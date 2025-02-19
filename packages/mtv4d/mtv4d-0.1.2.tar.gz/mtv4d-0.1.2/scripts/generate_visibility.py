from copy import deepcopy
import sys

from traitlets import ForwardDeclaredInstance

sys.path.append(".")

from tqdm import tqdm
from collections import defaultdict
from mtv4d.utils.draw_base import draw_boxes
import numpy as np
import os.path as op
from pathlib import Path as P
import torch
import cv2

from mtv4d.utils.box_base import to_corners_9, anno_box_to_9_values_box
from mtv4d.annos_4d.helper import anno_box_to_7_values_box, find_path_from_ts_and_dir_path, find_path_from_ts_and_dir_path_maybe_not_find, read_cal_data
from mtv4d.annos_4d.misc import boxes_to_corners_3d, read_ego_paths
from mtv4d.utils.geo_base import transform_pts_with_T
from mtv4d.utils.io_base import read_json, read_points_from_bin, read_points_from_pcd
from mtv4d.utils.o3d_base import draw_points, hpr_index, in_hull, open3d_hpr
from mtv4d.utils.sensors import get_camera_models, to_camera_xy
from mtv4d.utils.timestamp_base import Timestamps
from mtv4d.utils.misc_base import Time, defaultdict_lambda, mp_pool
from mtv4d.annos_4d.reusable_4d_functions import (
    find_near_points_index_of_visible_points,
    filter_ground_pts,
    index_has_near_point_vis,
    load_and_transfer_annos_from_map,
    load_and_transfer_dn_boxes_from_frame,
)

# TODO: check guard, some frames does not have visibility and label

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default="/ssd4/data/4d/20231028_150815")
parser.add_argument("--num_process", type=int, default=8)
parser.add_argument("--calibration_path")
parser.add_argument("--hpr_relative_path")
parser.add_argument("--trajectory_path")
parser.add_argument("--manual_label_path")


def draw_points_on_image_dbg(other_points, timestamp, polylines, points, visibility, sensor):
    # points = np.array([[np.sin(i /180 * 3.14), np.cos(i/180*3.14), 0] for i in range(360)])
    other_points = to_camera_xy(op.join(scene_root, "whole_scene/calib/calibration.yml"), sensor, other_points).astype("int")

    points = to_camera_xy(op.join(scene_root, "whole_scene/calib/calibration.yml"), sensor, points).astype("int")
    im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, "camera", sensor))
    im = cv2.imread(im_path)
    for i in other_points:
        cv2.circle(im, tuple(i), 1, (128, 255, 0), 1)
    for i, j in zip(points, visibility):
        if int(j):
            cv2.circle(im, tuple(i), 5, (0, 0, 255), 5)
    for vis, pts in zip(split_visibility(polylines, visibility), split_visibility(polylines, points)):
        if "1" in vis:
            clr = (255, 0, 0)
        else:
            clr = (0, 255, 0)
        cv2.polylines(im, [pts.reshape(-1, 2)], 0, clr, 2)
    save_path = f"/tmp/12344/{sensor}/{timestamp}.jpg"
    P(save_path).parent.mkdir(exist_ok=True, parents=True)
    cv2.imwrite(save_path, im)


def draw_points_on_image(timestamp, polylines, points, visibility, sensor):
    # points = np.array([[np.sin(i /180 * 3.14), np.cos(i/180*3.14), 0] for i in range(360)])
    points = to_camera_xy(op.join(scene_root, "whole_scene/calib/calibration.yml"), sensor, points).astype("int")
    im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, "camera", sensor))
    im = cv2.imread(im_path)
    for i, j in zip(points, visibility):
        if int(j):
            cv2.circle(im, tuple(i), 5, (0, 0, 255), 5)
    for vis, pts in zip(split_visibility(polylines, visibility), split_visibility(polylines, points)):
        if "1" in vis:
            clr = (255, 0, 0)
        else:
            clr = (0, 255, 0)
        cv2.polylines(im, [pts.reshape(-1, 2)], 0, clr, 2)
    save_path = f"/tmp/12345/{sensor}/{timestamp}.jpg"
    P(save_path).parent.mkdir(exist_ok=True, parents=True)
    cv2.imwrite(save_path, im)


def draw_box_on_image(timestamp, polylines, points, visibility, sensor):
    points = to_camera_xy(op.join(scene_root, "whole_scene/calib/calibration.yml"), sensor, points).astype("int")
    im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, "camera", sensor))
    im = cv2.imread(im_path)
    boxes = [i for i, v in zip(points.reshape(-1, 8, 2), visibility) if v]
    if len(boxes) > 0:
        draw_boxes(im, np.stack(boxes))
    save_path = f"/tmp/1234/abcd/{sensor}/{timestamp}.jpg"
    P(save_path).parent.mkdir(exist_ok=True, parents=True)
    cv2.imwrite(save_path, im)


def split_visibility(poly_objs, visibility):
    output = []
    for i in poly_objs:
        i = len(i)
        vis, visibility = visibility[:i], visibility[i:]
        output += [vis]
    return output


def split_polylines_with_track_id(data, poly_objs):
    output = []
    for i in poly_objs:
        assert len(i["vertices"]) % 3 == 0, "len of vertices error"
        num = int(len(i["vertices"]) / 3)
        track_id = i["obj_track_id"]
        vis, data = data[:num], data[num:]
        output += [(track_id, vis)]
    return output


def mesh_index(points):
    import open3d as o3d

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    tic = Time()
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    tic.toc()
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
    tic.toc()
    # 设置视点位置
    camera_location = np.array([0, 0, 0])

    # 计算视点到每个顶点的向量
    vertices = np.asarray(mesh.vertices)
    vectors = vertices - camera_location

    # 计算法线
    mesh.compute_vertex_normals()
    normals = np.asarray(mesh.vertex_normals)

    # 计算法线和向量的点积
    dot_products = np.sum(normals * vectors, axis=1)

    # 可见顶点的索引
    visible_indices = np.where(dot_products > 0)[0]
    return visible_indices


def filter_polyline3d(all_vertices, acc_pcl, get_near_points=False, filter_points_without_visible_points_nearby=True):
    # 一个函数实现一个功能，然后转坐标系这件事情可以放在别的函数中
    points = np.concatenate([all_vertices, acc_pcl])
    indices = np.array(hpr_index(points, radius=3000))

    assert get_near_points, "to get polyline visibility, we need near points to be visible"
    if get_near_points:  # 离可见polyline=也可见sed
        filter_inds = find_near_points_index_of_visible_points(all_vertices, indices[indices < len(all_vertices)])
        indices = np.concatenate([indices, filter_inds])

    visibility = "".join(["1" if i in indices else "0" for i in range(len(all_vertices))])
    return visibility


def filter_poly_fov_mask(all_vertices, calib_sensor):
    # all_filter = all_vertices[:, 2]>-1000
    # return all_vertices[all_filter], all_filter
    # TODO: check img shape
    mask1 = all_vertices[:, 2] > 0  # 首先在正面
    # all_filter = mask1
    # return all_vertices[all_filter], all_filter
    EPS_FLOAT32 = float(np.finfo(np.float32).eps)
    MAX_FLOAT32 = float(np.finfo(np.float32).max)

    FOV = calib_sensor["fov_fit"]
    DistCoeff = D = calib_sensor["D"]
    img_shape = calib_sensor["image_size"]
    CameraMat = K = calib_sensor["K"]
    xc = all_vertices[:, 0]
    yc = all_vertices[:, 1]
    zc = all_vertices[:, 2]
    r2 = xc * xc + yc * yc
    norm = np.sqrt(r2)
    theta = np.arctan2(norm, zc)
    FOV_ = FOV / 2 * np.pi / 180
    fov_mask = theta > FOV_
    if True:
        rho = theta + DistCoeff[0] * theta**3 + DistCoeff[1] * theta**5 + DistCoeff[2] * theta**7 + DistCoeff[3] * theta**9
        image_radius = np.sqrt((img_shape[1] / 2) ** 2 + (img_shape[0]) ** 2)
        focal = [CameraMat[0, 0], CameraMat[1, 1]]
        rho[fov_mask] = 2 * image_radius / focal[0]
        xn = rho * xc / norm
        yn = rho * yc / norm
        xn[norm < EPS_FLOAT32] = 0
        yn[norm < EPS_FLOAT32] = 0
        normalize_coordinates = np.concatenate([np.vstack([xn, yn]), np.ones((1, xn.shape[0]))], axis=0)
        pixel_coordinates = CameraMat[:3, :3] @ normalize_coordinates
        x_filter = np.logical_and(pixel_coordinates[0, :] > 0, pixel_coordinates[0, :] < img_shape[0])  # [1920, 1080]
        y_filter = np.logical_and(pixel_coordinates[1, :] > 0, pixel_coordinates[1, :] < img_shape[1])
        all_filter = x_filter & y_filter & ~fov_mask & mask1
    else:
        all_filter = ~fov_mask & mask1
    return all_vertices[all_filter], all_filter


def find_round_timestamps(ts, timestamps, file_dir, num=8):
    a = np.argsort(np.abs(np.array(timestamps) - ts))[20:100]  # 但不行，得找10个左右的。是否可以说明内容都有。
    output_idxs = sorted(a)[::10]
    output_ts = [timestamps[i] for i in output_idxs]
    filenames = [find_path_from_ts_and_dir_path_maybe_not_find(i, file_dir) for i in output_ts]
    return output_ts, filenames


def get_visibility_by_self_car_mask(points_camera, calib_path, calib, sensor, mask_path):
    camera_model = get_camera_models(calib_path, [sensor])[sensor]
    im_mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED) > 0
    w, h = calib[sensor]["image_size"]
    points_xy = camera_model.project_points(points_camera).astype("int")
    points_mask1 = (points_xy[:, 0] >= 0) * (points_xy[:, 0] < w) * (points_xy[:, 1] >= 0) * (points_xy[:, 1] < h)
    filtered_xy = points_xy[points_mask1]
    points_mask1[points_mask1] = im_mask[filtered_xy[:, 1], filtered_xy[:, 0]]
    return points_mask1


def calculate_visibility_poly(timestamp, sensor, scene_root, all_vertices_lidar, Twes, mask_path, calib_path):
    path = P(scene_root) / f"lidar/overlapped_lidar1"
    ground_lidar_path = P(scene_root) / f"ground/undistort_ground_lidar1"
    lidar_path = find_path_from_ts_and_dir_path(timestamp, path)
    acc_pcl = read_points_from_bin(lidar_path)[:, :3]  # 首先读入点云，lidar系
    # tss, fns = find_round_timestamps(timestamp, sorted(Twes.keys()), ground_lidar_path, num=8)
    # for nm, fn in zip(tss, fns):
    #     if fn is None: continue
    #     b = read_points_from_pcd(str(path / fn))
    #     b = transform_pts_with_T(b[:, :3], np.linalg.inv(calib["lidar1"]["T_es"]) @ np.linalg.inv(Twes[timestamp]) @ Twes[nm]) # ego系，需要calib转到lidar系
    #     acc_pcl = np.concatenate([acc_pcl, b])
    # acc_pcl = filter_ground_pts(scene_root, acc_pcl, timestamp, thres_dist=0.15)  # 过滤非地面点云，均在lidar系
    if "camera" in sensor:
        acc_pcl = transform_pts_with_T(acc_pcl, calib[sensor]["T_se"] @ calib["lidar1"]["T_es"])  # 转到sensor系
        all_vertices = transform_pts_with_T(all_vertices_lidar, calib["lidar1"]["T_es"]) + np.array([[0, 0, 0.2]])  # 转到ego系
        all_vertices = transform_pts_with_T(all_vertices, calib[sensor]["T_se"])  # 转到sensor系
        # 1 fov
        all_vertices_filtered, filter_selected_mask = filter_poly_fov_mask(all_vertices, calib[sensor])
        # 2 hpr
        visibility_ = np.zeros(len(all_vertices))
        visibility_[filter_selected_mask] = [i for i in filter_polyline3d(all_vertices_filtered, acc_pcl, get_near_points=True)]
        if True:  # Twice
            new_filter_selected_mask = ~visibility_.astype("bool") & filter_selected_mask
            new_all_vertices_filtered = all_vertices[new_filter_selected_mask]
            visibility_[new_filter_selected_mask] = [i for i in filter_polyline3d(new_all_vertices_filtered, acc_pcl, get_near_points=True)]
        # 3 mask
        # mask_path = op.join(scene_root, f"self_mask/camera/{sensor}.png")
        # calib_path = op.join(scene_root, f"calibration_center.yml")
        input_vertices = transform_pts_with_T(all_vertices_lidar[visibility_.astype("int") == 1], calib[sensor]["T_se"] @ calib["lidar1"]["T_es"])
        visibility_[visibility_.astype("int") == 1] = get_visibility_by_self_car_mask(input_vertices, calib_path, calib, sensor, mask_path)  # 返回一个mask

        visibility = "".join(visibility_.astype("int").astype("str"))
    else:
        visibility = filter_polyline3d(all_vertices_lidar, acc_pcl, get_near_points=True)

    return visibility, acc_pcl


def hpr_normals(points, origin):
    import open3d as o3d

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3] - origin)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    normals = np.array(pcd.normals)
    picked_inds = ((normals * points).sum(1) / np.linalg.norm(points, axis=1)) < -0.8
    return points[picked_inds]


def calculate_visibility_box_single(calib, timestamp, sensor, corners, scene_root):
    # passenger_car_volume = 4.8 * 1.8 * 1.6
    # path =  P(scene_root) / f"lidar/overlapped_lidar1"
    path = P(scene_root) / f"hidden_point_removal/occlusion_filter_lidar_{sensor}"  
    # path = P(scene_root) / f"to_remove_1000/{sensor}"  
    # path =  P(scene_root) / f"to_remove/{sensor}"
    lidar_path = find_path_from_ts_and_dir_path(timestamp, path)
    acc_pcl = read_points_from_bin(lidar_path)[:, :3]
    # acc_pcl = open3d_hpr(points, radius=None, view_point=calib[sensor]['T_es'][:3, 3])  # 在上一个步骤做完

    if sensor == "lidar1":  # TODO: 改回来
    # if True:  # 只在lidar系做处理，因为这个可能考虑到其他视角了。还是每一个相机视角也做这样一件事情
        path2 = P(scene_root) / f"lidar/undistort_static_lidar1"
        lidar_path = find_path_from_ts_and_dir_path(timestamp, path2)
        if lidar_path.endswith(".pcd"):
            points2 = read_points_from_pcd(lidar_path)[:, :3]  # ego系，转到lidar系
            points2 = transform_pts_with_T(points2, calib["lidar1"]["T_se"])
        elif lidar_path.endswith(".bin"):
            points2 = read_points_from_bin(lidar_path)[:, :3]  # 本来就是lidar系
        acc_pcl = np.concatenate([points2, acc_pcl], axis=0)

    visibility = []
    for bx in corners.reshape(-1, 8, 3):
        visibility += [int(in_hull(acc_pcl, bx).sum())]
    return visibility


def func_generate_poly_vis(data, draw_im=False):  # poly在world系
    timestamp, sensor, all_vertices, polylines, calib, Twes, scene_root, mask_path, calib_path = data
    vertices_lidar = transform_pts_with_T(all_vertices, calib["lidar1"]["T_se"] @ np.linalg.inv(Twes[timestamp]))
    # 转到lidar系。其中，output是所有点的visibility，p是所有visible的poly points
    output, p = calculate_visibility_poly(timestamp, sensor, scene_root, vertices_lidar, Twes, mask_path, calib_path)
    if draw_im and "camera" in sensor:
        draw_points_on_image(timestamp, polylines, transform_pts_with_T(all_vertices, calib[sensor]["T_se"] @ np.linalg.inv(Twes[timestamp])), output, sensor)
    return output


def func_generate_dnbox_vis(data, draw_im=False):
    timestamp, sensor, box_objs, calib, scene_root = data
    if len(box_objs) == 0:
        return []
    box_list = np.concatenate([to_corners_9(anno_box_to_9_values_box(bx)) for bx in box_objs]).reshape(-1, 3)
    corners_lidar = transform_pts_with_T(box_list, calib["lidar1"]["T_se"])  # ego 2 lidar
    output = calculate_visibility_box_single(calib, timestamp, sensor, corners_lidar, scene_root)
    if draw_im and "camera" in sensor:
        draw_box_on_image(timestamp, box_list, transform_pts_with_T(box_list, calib[sensor]["T_se"]), output, sensor)
    return output


def func_generate_mapbox_vis(data, draw_im=True):  # box在world系
    timestamp, sensor, box_objs, calib, scene_root = data
    if len(box_objs) == 0:
        return []
    box_list = np.concatenate([to_corners_9(anno_box_to_9_values_box(bx)) for bx in box_objs]).reshape(-1, 3)
    corners_lidar = transform_pts_with_T(box_list, calib["lidar1"]["T_se"] @ np.linalg.inv(Twes[timestamp]))  # world 2 ego 2 lidar
    output = calculate_visibility_box_single(calib, timestamp, sensor, corners_lidar, scene_root)
    if draw_im and "camera" in sensor:
        draw_box_on_image(timestamp, box_list, transform_pts_with_T(box_list, calib[sensor]["T_se"] @ np.linalg.inv(Twes[timestamp])), output, sensor)
    return output


if __name__ == "__main__":
    args = parser.parse_args()
    scene_root = args.scene_root
    calib = read_cal_data(op.join(scene_root, "whole_scene/calib/calibration.yml"))
    Twes, _ = read_ego_paths(op.join(scene_root, f"whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"))
    sensors = [
        "lidar1",
        "camera6",
        "camera1",
        "camera5",
        "camera8",
        "camera11",
        "camera2",
        "camera3",
        "camera4",
        "camera6",
        "camera7",
        "camera12",
        "camera15",
    ]
    timestamps = Timestamps(scene_root, sensors[1:]).timestamps_clean 

    # ------------------------------------------
    # poly vis
    # ------------------------------------------
    (P(scene_root) / "4d_anno_infos").mkdir(exist_ok=True, parents=True)
    if True:  # poly vis
        poly_objs = read_json(op.join(scene_root, "whole_scene/objects_on_the_map/polylines/trajectory_temp_horizontal_interpolate_carline.json"))
        polylines = [np.array(i["vertices"]).reshape(-1, 3) for i in poly_objs]
        all_vertices = np.concatenate(polylines).reshape(-1, 3)
        # # 做两个ind的筛除
        # timestamps = timestamps[:100]
        # timestamps = [i for i in timestamps if a < 1698476899464 and i< 1698476899464]
        calib_path = op.join(scene_root, "whole_scene/calib/calibration.yml")
        data = [(t, s, all_vertices, polylines, calib, Twes, scene_root,  
                 op.join(scene_root, f"self_mask/camera/{s}.png"), calib_path) for t in timestamps for s in sensors]
        output = mp_pool(func_generate_poly_vis, data, args.num_process)
        vis_ts2id, vis_id2ts = defaultdict(defaultdict_lambda), defaultdict(defaultdict_lambda)
        for a, b in zip(data, output):
            ts, sensor = a[:2]
            for track_id, vis in split_polylines_with_track_id(b, poly_objs):
                vis_ts2id[ts][track_id][sensor] = vis
        for ts, v in vis_ts2id.items():
            for tid, v2 in v.items():
                vis_id2ts[tid][ts] = v2
        torch.save([vis_ts2id, vis_id2ts], op.join(scene_root, "4d_anno_infos/vis_poly.pth"))
    # ------------------------------------------
    # dnbox vis
    # ------------------------------------------
    if True:  # box vis, 全部都在ego系中。
        dn_boxes_dict_ts2id, dn_boxes_dict_id2ts = load_and_transfer_dn_boxes_from_frame(
            op.join(scene_root, "whole_scene/objects_of_individual_frames/boxes"), timestamps
        )
        for k, v in dn_boxes_dict_id2ts.items():
            for ts, bx in v.items():
                if bx["obj_type"] in [
                    "class.traffic_facility.speed_bump",
                    "class.road_marker.arrow",
                    "class.parking.wheel_stopper",
                    "class.parking.text_icon",
                    "class.parking.parking_lock",
                    "class.road_marker.text",
                ]:
                    bx["psr"]["scale"]["z"] += 0.4
        data = [(t, s, [i for i in dn_boxes_dict_ts2id[t].values()], calib, scene_root) for t in timestamps for s in sensors]
        output = mp_pool(func_generate_dnbox_vis, data, args.num_process)
        vis_ts2id, vis_id2ts = defaultdict(defaultdict_lambda), defaultdict(defaultdict_lambda)
        for d, o in zip(data, output):
            ts, sensor = d[:2]
            assert len(dn_boxes_dict_ts2id[ts].keys()) == len(o)
            for track_id, vis in zip(dn_boxes_dict_ts2id[ts].keys(), o):
                vis_ts2id[ts][track_id][sensor] = vis
        for ts, v in vis_ts2id.items():
            for tid, v2 in v.items():
                vis_id2ts[tid][ts] = v2
        torch.save([vis_ts2id, vis_id2ts], op.join(scene_root, "4d_anno_infos/vis_dnbox.pth"))

    # ------------------------------------------
    # mapbox vis
    # ------------------------------------------
    if True:  # map box，全部在world系中。
        map_boxes = load_and_transfer_annos_from_map(op.join(scene_root, "whole_scene/objects_on_the_map/boxes/trajectory_temp_horizontal.json"))
        for k, box in map_boxes.items():
            if box["obj_type"] in [
                "class.traffic_facility.speed_bump",
                "class.road_marker.arrow",
                "class.parking.wheel_stopper",
                "class.parking.text_icon",
                "class.parking.parking_lock",
                "class.road_marker.text",
            ]:
                box["psr"]["scale"]["z"] += 0.4  # 一半是0.2

        # 做两个ind的筛选
        # timestamps = timestamps[:200]
        # timestamps = [i for i in timestamps if i < 1698476899464 and i < 1698476899464]
        data = [(t, s, [i for i in map_boxes.values()], calib, scene_root) for t in timestamps for s in sensors]
        output = mp_pool(func_generate_mapbox_vis, data, args.num_process)
        vis_ts2id, vis_id2ts = defaultdict(defaultdict_lambda), defaultdict(defaultdict_lambda)
        for d, o in zip(data, output):
            ts, sensor = d[:2]
            assert len(map_boxes.keys()) == len(o)
            for track_id, vis in zip(map_boxes.keys(), o):
                vis_ts2id[ts][track_id][sensor] = vis
        for ts, v in vis_ts2id.items():
            for tid, v2 in v.items():
                vis_id2ts[tid][ts] = v2
        torch.save([vis_ts2id, vis_id2ts], op.join(scene_root, "4d_anno_infos/vis_mapbox.pth"))







