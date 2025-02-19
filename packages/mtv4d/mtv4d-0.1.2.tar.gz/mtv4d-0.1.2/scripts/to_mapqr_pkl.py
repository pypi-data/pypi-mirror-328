from collections import defaultdict
import sys

from tqdm import tqdm
from pyquaternion import Quaternion

sys.path.append(".")
import pickle
from easydict import EasyDict
import yaml
import numpy as np
from scipy.spatial.transform import Rotation
import os.path as op
from pathlib import Path as P

from mtv4d.annos_4d.helper import find_path_from_ts_and_dir_path, read_json_to_list, read_ts_json
from mtv4d.annos_4d.misc import read_ego_paths, translate_output_geometry_to_psr, translate_psr_to_output_geometry, translate_psr_with_T


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default="/ssd1/data/4d/20230823_110018")


def read_pickle(path):
    with open(path, "rb") as f:
        a = pickle.load(f)
    return a


def write_pickle(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)


cameras = [
    "camera1",
    "camera11",
    "camera5",
    "camera8",
]

# 'lidar_path', 'token', 'sweeps', 'cams', 'lidar2ego_translation', 'lidar2ego_rotation', 'ego2global_translation', 'ego2global_rotation', 'timestamp', 'gt_boxes', 'gt_names', 'gt_velocity', 'num_lidar_pts', 'num_radar_pts', 'valid_flag'


def format_cal_data(cal_data):
    """
    generate extrinsic mat, camera intrinsic mat and distort coefficient
    """
    sids = list(cal_data.keys())
    # if 'cam_bev' in sids:
    #     sids.remove('cam_bev')
    for sid in sids:
        if "cameras" in cal_data[sid]["sensor_model"]:
            if not "muzza" in cal_data[sid]["sensor_model"].lower():  # only support opencv model
                focal = cal_data[sid]["focal"]
                pp = cal_data[sid]["pp"]
                K = np.eye(3)
                if isinstance(focal, list):
                    K[0, 0], K[1, 1] = focal
                else:
                    K[0, 0], K[1, 1] = focal, focal
                K[0, 2], K[1, 2] = pp
                cal_data[sid]["K"] = K
                if "inv_poly" in cal_data[sid].keys():
                    cal_data[sid]["D"] = np.array(cal_data[sid]["inv_poly"])
        if "extrinsic" in cal_data[sid].keys():
            tx, ty, tz, qx, qy, qz, qw = cal_data[sid]["extrinsic"]
            T = np.eye(4)
            q = Rotation.from_quat([qx, qy, qz, qw])
            if hasattr(q, "as_dcm"):
                T[:3, :3] = q.as_dcm().astype("float32")
            else:
                T[:3, :3] = q.as_matrix().astype("float32")
            T[:3, 3] = np.array([tx, ty, tz])
            cal_data[sid]["T_es"] = T
            cal_data[sid]["T_se"] = np.linalg.inv(T)


def read_cal_data(yaml_file):
    with open(yaml_file) as f:
        rig_data = yaml.load(f, Loader=yaml.FullLoader)
        rig_data = EasyDict(rig_data)
        cal_data = rig_data.rig
        format_cal_data(cal_data)
    return cal_data


def get_cams_info(calib):
    cams_info = defaultdict(dict)
    for cam in cameras:
        # cams_info[cam]["extrinsic"] = calib[cam]["extrinsic"]
        cams_info[cam]["focal"] = calib[cam]["focal"]
        cams_info[cam]["fov_fit"] = calib[cam]["fov_fit"]
        cams_info[cam]["inv_poly"] = calib[cam]["inv_poly"]
        cams_info[cam]["poly"] = calib[cam]["poly"]
        cams_info[cam]["pp"] = calib[cam]["pp"]
        cams_info[cam]["image_size"] = calib[cam]["image_size"]
        cams_info[cam]["K"] = calib[cam]["K"]
        cams_info[cam]["D"] = calib[cam]["D"]
        cams_info[cam]["Tes"] = calib[cam]["T_es"]
        cams_info[cam]["Tse"] = calib[cam]["T_se"]
        cams_info[cam]["Tlc"] = calib["lidar1"]["T_se"] @ calib[cam]["T_es"]
        cams_info[cam]["Tcl"] = calib["lidar1"]["T_es"] @ calib[cam]["T_se"]
        cams_info[cam]["intr_dict"] = {
            "image_size": calib[cam]["image_size"],
            "focal": calib[cam]["focal"],
            "fov_fit": calib[cam]["fov_fit"],
            "inv_poly": calib[cam]["inv_poly"],
            "poly": calib[cam]["poly"],
            "pp": calib[cam]["pp"],
            "K": calib[cam]["K"],
            "D": calib[cam]["D"],
        }
    return cams_info


def generate_lidar_sweep_info(ts, lidar_path, calib, Twes, ts0):
    path = find_path_from_ts_and_dir_path(ts, lidar_path)
    output = {
        # "data_path": path,
        "data_path": op.join("data/mtv", scene_name, str(P(path).relative_to(scene_root))),
        "type": "lidar",
        "sample_data_token": 1,
        "timestamp": ts,
    }
    output["sensor2ego_translation"] = calib["lidar1"]["T_es"][:3, 3]
    output["sensor2ego_rotation"] = to_cmt_pyquaternion(calib["lidar1"]["T_es"][:3, :3])
    output["ego2global_translation"] = Twes[ts][:3, 3]
    output["ego2global_rotation"] = to_cmt_pyquaternion(Twes[ts][:3, :3])
    Te0w = np.linalg.inv(Twes[ts0]) 
    Twet = Twes[ts]
    Te0et = Te0w @Twet
    output["sensor2lidar_translation"] = Te0et[:3, 3]  # 这个是to ego0的sensor,这个lidar是原始帧的lidar
    output["sensor2lidar_rotation"] = Te0et[:3, :3]
    return output


def find_prev_ten_lidar_path(ts):
    ts_list = np.array(timestamps)
    idx = np.where(ts_list == ts)[0][0]
    id_min = max(0, idx - 9)
    tses = ts_list[id_min : idx + 1].tolist()
    return tses


def box3d_to_pred_array(box):
    output = []
    if "pos_xyz" not in box.keys():
        assert False, "box input format error"
    output = box["pos_xyz"] + box["scale_xyz"] + [box["rot_xyz"][-1]]
    # output = box["pos_xyz"] + box["scale_xyz"] + box["rot_xyz"]
    return np.array(output)


def to_cmt_pyquaternion(R):
    q = Rotation.from_matrix(R).as_quat()  # xyzw
    return q[[3, 0, 1, 2]]


def generate_mapqr_pkl_one(boxes, calib, cams_info):
    # cams_info 从另一个角度进行记录
    # 这里所有的数据最好转到lidar系，因为模型训练给的是lidar系。是否需要在pkl中就转好坐标系呢。
    ts = boxes[0]["timestamp"]
    output = {}
    lidar_dir = op.join(scene_root, "lidar/undistort_static_lidar1")
    lidar_path = find_path_from_ts_and_dir_path(ts, lidar_dir)
    output["lidar_path"] = op.join("data/mtv", scene_name, str(P(lidar_path).relative_to(scene_root)))
    output["token"] = 1
    output["sweeps"] = [generate_lidar_sweep_info(i, lidar_dir, calib, Twes, ts) for i in find_prev_ten_lidar_path(ts)]
    cam_outs = {}
    for cam in cameras:
        cam_dir = op.join(scene_root, "camera", cam)
        cam_path = find_path_from_ts_and_dir_path(ts, cam_dir)
        out = {
            "data_path": op.join("data/mtv", scene_name, str(P(cam_path).relative_to(scene_root))),
            "type": cam,
            "sample_data_token": 1,  # TODO:
            "sensor2ego_translation": cams_info[cam]["Tes"][:3, 3],
            "sensor2ego_rotation": to_cmt_pyquaternion(cams_info[cam]["Tes"][:3, :3]),
            "ego2global_translation": cams_info[cam]["Tse"][:3, 3],
            "ego2global_rotation": to_cmt_pyquaternion(cams_info[cam]["Tse"][:3, :3]),
            "timestamp": ts,
            "sensor2lidar_translation": cams_info[cam]["Tlc"][:3, 3],
            "sensor2lidar_rotation": cams_info[cam]["Tlc"][:3, :3],
            "cam_intrinsic": cams_info[cam]["intr_dict"],
        }
        cam_outs[cam] = out
    output["cams"] = cam_outs
    output["lidar2ego_translation"] = calib["lidar1"]["T_es"][:3, 3]
    output["lidar2ego_rotation"] = to_cmt_pyquaternion(calib["lidar1"]["T_es"][:3, :3])
    output["ego2global_translation"] = Twes[ts][:3, 3]
    output["ego2global_rotation"] = to_cmt_pyquaternion(Twes[ts][:3, :3])
    output["timestamp"] = ts
    output['prev'] = None
    output['next'] = None
    output['scene_token'] = P(scene_name).name
    output['can_bus'] = np.zeros(18)
    output['frame_idx'] = idx_t
    output['map_location'] =  Twes[ts][:3, 3]

    def transfer_poly_with_T(poly, T):
        T = np.array(T)
        poly = np.array(poly).reshape(-1, 3)
        poly = np.concatenate([poly, np.ones([len(poly), 1])], axis=1)
        return (T @ poly.T).T[:, :3].tolist()

    Tew = np.linalg.inv(Twes[ts])
    output_label_list = [
        "class.parking.parking_slot",
        "class.road_marker.arrow_heading_triangle",
        "class.road_marker.lane_line",
        "class.road_marker.no_parking_zone",
        ]
    split_list = [ "class.road_marker.lane_line"]

    def split_visibility(vis):
        vis1 = [i and j for i, j in zip(vis[:-1], vis[1:])]
        vis2 = [False] + vis1 + [False]
        data = [j-i for i, j in zip(vis2[:-1], vis2[1:])]
        st = [i for i, d in enumerate(data) if d == 1]
        ed = [i for i, d in enumerate(data) if d == -1]
        output = [(i, j) for i, j in zip(st, ed)]
        return output

    def split_pts(pts, vis):
        output_parts=[]
        split_parts = split_visibility(vis)
        for a, b in split_parts:
            output_parts += [pts[a:b+1]]
        return output_parts
    
    def get_poly_frame(polys, type_name, T, split=False):
        output = []
        for poly in polys:
            if poly["obj_type"] != type_name: continue
            pts = poly["geometry"]
            vis = [any([v[i]=='1' for k, v in poly['visibility'].items()]) for i in range(len(pts))]
            if sum(vis) < 2: continue
            new_pts = transfer_poly_with_T(pts, T)   # transfer from ego to lidar, while lidar is ego
            if split: 
                output += split_pts(new_pts, vis)
            else:
                output += [new_pts]
        return output  
    
    Tle =  calib["lidar1"]["T_se"] 
    output["annotation"] = {k: get_poly_frame(boxes, k, Tle, k in split_list) for k in output_label_list}
    return output


if __name__ == "__main__":

    args = parser.parse_args()
    scene_root = args.scene_root
    scene_name = P(scene_root).name
    traj_p = op.join(scene_root, f"trajectory.txt")
    Twes, _ = read_ego_paths(traj_p)
    calib = read_cal_data(op.join(scene_root, "calibration_center.yml"))
    calib["lidar1"]["T_es"] = np.eye(4)
    calib["lidar1"]["T_se"] = np.eye(4)
    cams_info = get_cams_info(calib)
    timestamps, _ = read_ts_json(op.join(scene_root, "4d_anno_infos/ts.json"))
    box_dir = op.join(scene_root, "4d_anno_infos/4d_anno_infos_frame/frames_labels")
    pkl_data_list = []
    for idx_t, ts in tqdm(enumerate(timestamps), desc="transforming to mapqr, ts"):
        polys = read_json_to_list(op.join(box_dir, f"{int(ts)}.json"))
        polys = [i for i in polys if i["geometry_type"] == "polyline3d"]
        pkl_data_list += [generate_mapqr_pkl_one(polys, calib, cams_info)]  # one timestamp; and needs to filter out data
    # write_pickle({"infos": pkl_data_list, "metadata": {"version": "v1.0-trainval"}}, op.join(scene_root, f"4d_anno_infos/cmt_pkl_lidarego_9d.pkl"))
    write_pickle({"infos": pkl_data_list, "metadata": {"version": "v1.0-trainval"}}, op.join(scene_root, f"4d_anno_infos/mapqr_pkl_lidar_ego.pkl"))

# scp /ssd1/data/4d/20230823_110018/4d_anno_infos/mapqr_pkl_lidar_ego.pkl yuanshiwei@192.168.23.222:/ssd1/data/4d/20230823_110018/4d_anno_infos/
# scp /ssd1/data/4d1/20230823_110018/4d_anno_infos/mapqr_pkl_lidar_ego.pkl yuanshiwei@192.168.23.223:/ssd1/data/4d/20230823_110018/4d_anno_infos/
# scp /ssd1/data/4d1/20231103_174738/4d_anno_infos/mapqr_pkl_lidar_ego.pkl yuanshiwei@192.168.23.223:/ssd1/data/4d/20231103_174738/4d_anno_infos/

# 7个数字和ego等信息。

"""
    python scripts/to_mapqr_pkl.py --scene_root /ssd1/data/4d/20231103_174738
    python scripts/to_mapqr_pkl.py --scene_root /ssd1/data/4d/20230823_110018
"""