from os import times
import sys


sys.path.append('.')
import numpy as np
import open3d as o3d
import os.path as op
from pathlib import Path as P
from tqdm import tqdm
from mtv4d.annos_4d.helper import torch_pool
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--scene_root",  default="/ssd1/data/4d/20231028_150815")
parser.add_argument("--num_process", type=int, default=8)


def read_bin(path):
    return np.fromfile(path, dtype=np.float32).reshape(-1, 4)


def write_bin(data, path):
    P(path).parent.mkdir(exist_ok=True, parents=True)
    data.tofile(str(path))


def draw_points(points, save_path="output.ply"):
    add_points = np.zeros([300, 3])
    add_points[:100, 0] = np.arange(100) / 10
    add_points[100:200, 1] = np.arange(100) / 10
    add_points[200:, 2] = np.arange(100) / 10
    points = np.concatenate([points, add_points])
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    P(save_path).parent.mkdir(parents=True, exist_ok=True)
    o3d.io.write_point_cloud(save_path, pcd)


def open3d_hpr(points, view_point=None, radius=None):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    viewpoint = np.array([0, 0, 0]) if view_point is None else view_point
    radius = radius if radius is not None else np.abs(np.linalg.norm(points[:, :3]-viewpoint, axis=-1)).max() * 100
    _, pt_map = pcd.hidden_point_removal(viewpoint, radius)
    return points[np.array(sorted(pt_map))]


def open3d_scipy(points,view_point=None, radius=None):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    viewpoint = np.array([0, 0, 0]) if view_point is None else view_point
    radius = radius if radius is not None else np.abs(np.linalg.norm(points[:, :3]-viewpoint, axis=-1)).max() * 100
    _, pt_map = pcd.hidden_point_removal(viewpoint, radius)
    return points[np.array(sorted(pt_map))]


def hidden_point_generate(path):
    scene_root = root_path = P(path).parent.parent.parent  # "lidar/overlapped_lidar1"
    points = read_bin(str(path))
    points = open3d_hpr(points, view_point=None)
    from mtv4d.utils.calib_base import read_cal_data, read_ego_paths
    calib = read_cal_data(op.join(scene_root, "whole_scene/calib/calibration.yml"))
    # save_path = op.join(root_path, "hidden_point_removal/occlusion_filter_lidar_lidar1", path.name)
    save_path = op.join("/tmp/1234/save_hpr/", P(path).name)
    # save_path = "/tmp/1234/save_hpr/2.bin"
    write_bin(points, save_path)
    if False:
        from mtv4d.utils.box_base import anno_box_to_9_values_box, to_corners_9
        from mtv4d.utils.calib_base import read_cal_data, read_ego_paths
        from mtv4d.utils.geo_base import transform_pts_with_T
        from mtv4d.utils.io_base import read_json
        from mtv4d.utils.box_base import box_corners_to_dot_cloud
        timestamp = float(P(path).stem.split('_')[-1])
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
        draw_points(pp, '/tmp/1234/kuang.ply')
        exit()

if __name__ == "__main__":
    args = parser.parse_args()
    root_path = args.scene_root
    lidar_path = op.join(root_path, "lidar/overlapped_lidar1")
    paths = sorted(P(lidar_path).glob("*.*"))
    path = '/ssd4/data/4d/20231028_150815/lidar/overlapped_lidar1/000080_1698476903764.bin'
    hidden_point_generate(path)
    # torch_pool(hidden_point_generate, paths, args.num_process)




