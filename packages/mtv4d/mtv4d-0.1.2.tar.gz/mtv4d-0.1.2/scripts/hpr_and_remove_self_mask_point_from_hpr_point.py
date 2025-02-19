import sys
sys.path.append(".")
from pathlib import Path as P
from mtv4d.utils.geo_base import transform_pts_with_T
import cv2
from mtv4d.utils.io_base import read_points_from_bin, write_bin
from mtv4d.utils.sensors import get_camera_models
from pathlib import Path as P
from mtv4d.annos_4d.helper import torch_pool
import argparse
from mtv4d.utils.calib_base import read_cal_data
import numpy as np
import open3d as o3d
import os.path as op


parser = argparse.ArgumentParser()
parser.add_argument("--input-hpr-dir", default="/ssd4/data/4d/20231028_150815/lidar/overlapped_lidar1")
parser.add_argument("--calibration-path", default="/ssd4/data/4d/20231028_150815/calibration_center.yml")
parser.add_argument("--self-mask-path", default="/ssd4/data/4d/20231028_150815/self_mask/camera/camera11.png")
parser.add_argument("--output-hpr-dir", default="/ssd4/data/4d/20231028_150815/to_remove_1000")
parser.add_argument("--hpr-radius", default=1000)
parser.add_argument("--sensor-id", type=str, default="camera11")
parser.add_argument("--generate_all_sensor", action='store_true', default=False)
parser.add_argument("--num_process", type=int, default=8)
parser.add_argument("--hpr-suffix", default=".bin")
parser.add_argument("--hpr-coord-sys", choices=["ego", "lidar1"], default="lidar1")


def hidden_point_generate(path):
    # root_path = P(path.parent.parent.parent)  # "lidar/overlapped_lidar1"
    # path = P('/ssd4/data/4d/20231028_150815') / "hidden_point_removal/occlusion_filter_lidar_camera6/000405_1698476936264.bin"
    # root_path = "/ssd4/data/4d/20231028_150815"
    root_path = '/ssd4/data/4d/20231107_123645/'
    points = read_points_from_bin(str(path))
    # points = open3d_hpr(points, view_point=None)
    # save_path = op.join(root_path, "hidden_point_removal/occlusion_filter_lidar_camera11", path.name)
    # write_bin(points, save_path) 
    if True:
        from mtv4d.utils.box_base import anno_box_to_9_values_box, to_corners_9
        from mtv4d.utils.calib_base import read_cal_data, read_ego_paths
        from mtv4d.utils.geo_base import transform_pts_with_T
        from mtv4d.utils.io_base import read_json
        from mtv4d.utils.box_base import box_corners_to_dot_cloud

        timestamp = float(P(path).stem.split("_")[-1])
        Twes, _ = read_ego_paths(op.join(root_path, f"whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"))
        if timestamp not in Twes.keys():
            return
        print(timestamp)
        calib = read_cal_data(op.join(root_path, "whole_scene/calib/calibration.yml"))
        box_objs = read_json(op.join(root_path, "whole_scene/objects_on_the_map/boxes/trajectory_temp_horizontal.json"))
        box_list = np.concatenate([to_corners_9(anno_box_to_9_values_box(bx)) for bx in box_objs]).reshape(-1, 3)
        corners_lidar = transform_pts_with_T(box_list, calib["lidar1"]["T_se"] @ np.linalg.inv(Twes[timestamp]))
        box_points = box_corners_to_dot_cloud(corners_lidar)
        pp = np.concatenate([points[:, :3], box_points])
        from tmp_scripts.save_pcd_with_box_labels import draw_points
        draw_points(pp, "/tmp/1234/kuang1.ply")
        exit()


def open3d_hpr(points, view_point=None, radius=None):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    viewpoint = np.array([0, 0, 0]) if view_point is None else view_point
    radius = radius if radius is not None else np.abs(np.linalg.norm(points[:, :3] - viewpoint, axis=-1)).max() * 100
    _, pt_map = pcd.hidden_point_removal(viewpoint, radius)
    return points[np.array(sorted(pt_map))]


def remove_fov_from_lidar_points(data):
    points, sensor, calib = data
    # assert points is lidar points
    T_cl = calib[sensor]["T_se"] @ calib["lidar1"]["T_es"]
    fov = calib[sensor]["fov_fit"]
    fov_cos_thres = np.cos(fov / 2 / 180 * np.pi)
    points_lidar = points[:, :3]
    points_camera = transform_pts_with_T(points_lidar, T_cl)
    a = points_camera / np.linalg.norm(points_camera, axis=1).reshape(-1, 1) @ np.array([0, 0, 1])
    return points[a > fov_cos_thres]  # 是remove fov好，还是return mask好


def remove_self_mask_from_hpr(data):  # input point: lidar coord
    points, sensor, calib, camera_model, im_mask = data
    w, h = calib[sensor]["image_size"]

    T_cl = calib[sensor]["T_se"] @ calib["lidar1"]["T_es"]
    points_lidar = points[:, :3]
    points_camera = transform_pts_with_T(points_lidar, T_cl)
    points_xy = camera_model.project_points(points_camera).astype("int")
    points_mask1 = (points_xy[:, 0] >= 0) * (points_xy[:, 0] < w) * (points_xy[:, 1] >= 0) * (points_xy[:, 1] < h)
    filtered_xy = points_xy[points_mask1]
    visible_mask = im_mask[filtered_xy[:, 1], filtered_xy[:, 0]]
    points_filtered = points[points_mask1][visible_mask]
    return points_filtered


def generate_hpr_and_remove_image_mask(data):
    overlapped_path, src_dir, save_dir, sensor, calib, camera_model, im_mask, hpr_radius = data

    points = read_points_from_bin(str(overlapped_path))
    T_lc = calib["lidar1"]["T_se"] @ calib[sensor]["T_es"]
    # 1 generate hpr
    points = open3d_hpr(points, T_lc[:3, 3], radius=hpr_radius)
    # 2 remove camera_fov
    if "camera" in sensor:
        data = (points, sensor, calib)
        points = remove_fov_from_lidar_points(data)
    # #  3 remove mask
    if "camera" in sensor:
        data = (points, sensor, calib, camera_model, im_mask)
        points = remove_self_mask_from_hpr(data)

    save_path = P(save_dir) / P(overlapped_path).relative_to(src_dir)
    save_path.parent.mkdir(exist_ok=True, parents=True)
    write_bin(points, save_path)


if __name__ == "__main__":
    args = parser.parse_args()
    assert args.hpr_suffix == ".bin", "not implement {} coord".format(args.hpr_suffix)
    assert args.hpr_coord_sys == "lidar1", "not implement {} coord".format(args.coord_sys)
    sensor = args.sensor_id
    src_dir = args.input_hpr_dir
    scene_root = P(src_dir).parent.parent
    dst_dir = args.output_hpr_dir if args.output_hpr_dir is not None else src_dir
    calib_path = args.calibration_path
    mask_path = args.self_mask_path
    hpr_radius = None if args.hpr_radius is None or args.hpr_radius == 'None' else float(args.hpr_radius)
    cameras = ["camera6", "camera8", "camera1", "camera5", "camera11", "camera13", "camera2", "camera3", "camera4", "camera7", "camera15", "camera12"]
    calib = read_cal_data(args.calibration_path)
    camera_models = get_camera_models(calib_path, None)
    hpr_paths = sorted(P(src_dir).glob(f"*{args.hpr_suffix}"))
    if args.generate_all_sensor:  # generate every sensor
        camera_models = get_camera_models(calib_path, cameras)
        im_masks = {cam: cv2.imread(op.join(scene_root, f"self_mask/camera/{cam}.png"), cv2.IMREAD_UNCHANGED) > 0 for cam in cameras}
        data = []
        for i in hpr_paths:
            for sensor in cameras:
                data += [(str(i), src_dir, op.join(dst_dir, sensor), sensor, calib, camera_models[sensor], im_masks[sensor], hpr_radius)]
            data += [(str(i), src_dir, op.join(dst_dir, "lidar1"), "lidar1", calib, None, None, None)]
    else:  # generate the given one sensor
        if 'camera' in sensor:
            camera_model = camera_models[sensor]
            im_mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED) > 0
            data = [(str(i), src_dir, dst_dir, sensor, calib, camera_model, im_mask, hpr_radius) for i in hpr_paths]
        else:
            data = [(str(i), src_dir, dst_dir, sensor, calib, None, None, None) for i in hpr_paths]
    torch_pool(generate_hpr_and_remove_image_mask, data, args.num_process)
