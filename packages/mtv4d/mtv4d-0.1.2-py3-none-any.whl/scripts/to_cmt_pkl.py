from collections import defaultdict
import sys

sys.path.append(".")

from tqdm import tqdm
from mtv4d.utils.box_base import translate_output_geometry_to_psr, translate_psr_to_output_geometry, translate_psr_with_T
from mtv4d.utils.calib_base import read_ego_paths
from mtv4d.utils.io_base import read_json
from mtv4d.utils.misc_base import find_path_from_ts_and_dir_path, get_times
from mtv4d.utils.timestamp_base import Timestamps
import pickle
from easydict import EasyDict
import yaml
import numpy as np
from scipy.spatial.transform import Rotation
import os.path as op
from pathlib import Path as P
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('--scene_root', default='/ssd1/data/4d/20231103_174738')
# parser.add_argument('--scene_root', default='/ssd3/yuanshiwei/4d_test/20231028_150815')
parser.add_argument("--scene_root", default="/ssd1/data/4d/20230831_151057")
# parser.add_argument("--scene_root", default="/ssd1/data/4d/20230823_110018")


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


def format_cal_data(cal_data):
    """
    generate extrinsic mat, camera intrinsic mat and distort coefficient
    """
    sids = list(cal_data.keys())
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
        "data_path": op.join("data/mtv", scene_name, str(P(path).relative_to(scene_root))),
        "type": "lidar",
        "sample_data_token": 1,
        "timestamp": ts,
    }
    output["sensor2ego_translation"] = calib["lidar1"]["T_es"][:3, 3]
    output["sensor2ego_rotation"] = to_cmt_pyquaternion(calib["lidar1"]["T_es"][:3, :3])
    output["ego2global_translation"] = Twes[ts][:3, 3]  # 每一帧点云ts对应的 ego2global的数据
    output["ego2global_rotation"] = to_cmt_pyquaternion(Twes[ts][:3, :3])

    Te0w = np.linalg.inv(Twes[ts0])
    Twet = Twes[ts]
    Te0et = Te0w @ Twet
    output["sensor2lidar_translation"] = Te0et[:3, 3]  # 这个是to ego0的sensor,这个lidar是原始帧的lidar； 当前帧的lidar对应的lidar0的变化
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


def generate_cmt_pkl_one(ts, boxes, calib, cams_info):
    # cams_info 从另一个角度进行记录
    # 这里所有的数据最好转到lidar系，因为模型训练给的是lidar系。是否需要在pkl中就转好坐标系呢。
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
            "sample_data_token": 1,
            "sensor2ego_translation": cams_info[cam]["Tes"][:3, 3],
            "sensor2ego_rotation": to_cmt_pyquaternion(cams_info[cam]["Tes"][:3, :3]),
            "ego2global_translation": Twes[ts][:3, 3],
            "ego2global_rotation": to_cmt_pyquaternion(Twes[ts][:3, :3]),
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
    output["ego2global_rotation"] = Twes[ts][:3, :3]
    output["timestamp"] = ts
    output["gt_boxes"] = np.array(
        [
            box3d_to_pred_array(
                translate_psr_to_output_geometry(translate_psr_with_T(translate_output_geometry_to_psr(b["geometry"]), calib["lidar1"]["T_se"]))
            )
            for b in boxes
        ]
    )
    output["gt_names"] = [b["obj_type"] for b in boxes]
    output["gt_velocity"] = np.array([b["velocity"] for b in boxes])
    output["num_lidar_pts"] = np.array([b["visibility"]["lidar1"] for b in boxes])
    output["num_radar_pts"] = 0
    output["valid_flag"] = [i > 0 for i in output["num_lidar_pts"]]
    return output


if __name__ == "__main__":

    args = parser.parse_args()
    scene_root = args.scene_root
    scene_name = P(scene_root).name
    calib = read_cal_data(op.join(scene_root, "calibration_center.yml"))
    calib["lidar1"]["T_es"] = np.eye(4)
    calib["lidar1"]["T_se"] = np.eye(4)
    cams_info = get_cams_info(calib)
    Twes, _ = read_ego_paths(op.join(scene_root, f"trajectory.txt"))
    # timestamps = Timestamps.from_json(scene_root, cameras).timestamps_clean
    # timestamps = Timestamps(scene_root, cameras).timestamps_clean
    pkl_data_list = []

    box_dir = op.join(scene_root, "4d_anno_infos/4d_anno_infos_frame/frames_labels")
    timestamps, _ = get_times(box_dir)
    for ts in tqdm(timestamps, desc="transforming to cmt, ts"):
        boxes = read_json(op.join(box_dir, f"{int(ts)}.json"))
        boxes = [i for i in boxes if i["geometry_type"] == "box3d"]
        pkl_data_list += [generate_cmt_pkl_one(ts, boxes, calib, cams_info)]
    write_pickle({"infos": pkl_data_list, "metadata": {"version": "v1.0-trainval"}}, op.join(scene_root, f"4d_anno_infos/cmt_pkl_lidar_ego.pkl"))

# trajectory.txt calibration_center.yml 4d_anno_infos
