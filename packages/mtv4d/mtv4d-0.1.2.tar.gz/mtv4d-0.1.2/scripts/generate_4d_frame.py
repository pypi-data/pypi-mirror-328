# s3://mv-4d-annotation/AutoCollaborator/manual_annotation/baidu500/20230823_110018/whole_scene/
# s3://mv-4d-annotation/data/multimodel_data_baidu/20230823_110018/3d_box/3d_box_sync

# manual_map_box
# manual_frame_box
# infer_box

"""
实现功能
1 从4d json中 根据visibility 生成 sub_id, 对于此三类都要生成sub_id
    被遮挡的部分不在frame中存储
2 所有frame的标注都转到ego系中; 其中4d json均在world中
"""

import sys

sys.path.append(".")
import warnings

warnings.filterwarnings("ignore")
from mtv4d.utils.box_base import translate_psr_to_output_geometry, translate_psr_with_T
from mtv4d.utils.calib_base import read_cal_data, read_ego_paths
from mtv4d.utils.geo_base import transform_pts_with_T
from mtv4d.utils.io_base import read_json, write_json_from_list
from mtv4d.utils.timestamp_base import Timestamps
import os.path as op
from collections import defaultdict
from copy import deepcopy
import numpy as np
from pathlib import Path as P
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default="/ssd1/data/4d/20230823_110018")


label_to_class = {
    "101": "Box_truck",
    "102": "Truck",
    "103": "Car",
    "104": "Van",
    "105": "Bus",
    "106": "Engineering_vehicle",
    "201": "Pedestrian",
    "202": "Cyclist",
    "301": "Bicycle",
    "100": "DontCare",
}


# -------------------------------
# --- generate output
# -------------------------------


def generate_frame_info_box(frame_boxes, ts, varying_state):
    # applicable to varying & not_varying
    # varying_state: 0: varying, 1: not_varying
    frame_info = []
    for track_id, box in frame_boxes.items():
        # if varying_state == 'not_varying':
        if "sub_id" not in box.keys():
            continue  # 表示不可见
        else:
            track_id = f'{track_id}_{box["sub_id"]}'

        box_single_info = {
            "obj_type": box["obj_type"],
            "obj_track_id": track_id,
            "obj_time_varying_state": varying_state,
            "geometry_type": "box3d",
            "timestamp": ts,
            "obj_attr": {} if "obj_attr" not in box.keys() and varying_state == "varying" else box["obj_attr"],
            "visibility": box["visibility"],
            "velocity": box["velocity"],
            "geometry": box["psr_ego"],
        }
        frame_info.append(box_single_info)
    return frame_info


def generate_frame_info_polyline(frame_polylines, ts):
    frame_info = []
    for track_id, poly in frame_polylines.items():
        if "sub_id" not in poly.keys():
            continue  # 表示不可见
        else:
            track_id = f'{track_id}_{poly["sub_id"]}'

        polyline_single_info = {
            "obj_type": poly["obj_type"],
            "obj_track_id": track_id,
            "obj_time_varying_state": "not_varying",
            "geometry_type": "polyline3d",
            "timestamp": ts,
            "obj_attr": poly["obj_attr"],
            "visibility": poly["visibility"],
            "geometry": poly["vertices_ego"],
        }
        frame_info.append(polyline_single_info)
    return frame_info


def generate_4d_frame_json_data(dn_boxes_vis_dict_id2ts, map_boxes_vis_dict_id2ts, map_polylines_vis_dict_id2ts):

    output_4d_frame_json = defaultdict(list)

    for ts, frame_box_dict in dn_boxes_vis_dict_id2ts.items():
        boxes_info = generate_frame_info_box(frame_box_dict, ts, varying_state="varying")
        output_4d_frame_json[ts] += boxes_info

    for ts, frame_box_dict in map_boxes_vis_dict_id2ts.items():
        boxes_info = generate_frame_info_box(frame_box_dict, ts, varying_state="not_varying")
        output_4d_frame_json[ts] += boxes_info

    for ts, polylines in map_polylines_vis_dict_id2ts.items():
        polylines_info = generate_frame_info_polyline(polylines, ts)
        output_4d_frame_json[ts] += polylines_info

    return output_4d_frame_json


def update_box_with_world_lidar_psr(box, world_T, ego_T):
    psr = box["psr"]
    box["psr_world"] = translate_psr_to_output_geometry(translate_psr_with_T(psr, world_T))
    box["psr_ego"] = translate_psr_to_output_geometry(translate_psr_with_T(psr, ego_T))


def update_poly_with_world_lidar_vertices(polyline, world_T, ego_T):
    vertices = polyline["vertices"]
    polyline["vertices_world"] = transform_pts_with_T(vertices, world_T).tolist()
    polyline["vertices_ego"] = transform_pts_with_T(vertices, ego_T).tolist()


def translate_output_geometry_to_psr(box):
    x, y, z = box["pos_xyz"]
    a, b, c = box["scale_xyz"]
    rx, ry, rz = box["rot_xyz"]
    return {"position": {"x": x, "y": y, "z": z}, "scale": {"x": a, "y": b, "z": c}, "rotation": {"x": rx, "y": ry, "z": rz}}


def generate_DS4d_from_4dMapJson(data_path, Twes):
    output_json_list = read_json(data_path)
    dn_boxes_vis_dict_ts2id, map_boxes_vis_dict_ts2id = defaultdict(dict), defaultdict(dict)
    dn_boxes_vis_dict_id2ts, map_boxes_vis_dict_id2ts = defaultdict(dict), defaultdict(dict)
    map_polylines_vis_dict_ts2id, map_polylines_vis_dict_id2ts = defaultdict(dict), defaultdict(dict)
    for box_dict in tqdm(output_json_list, desc="generating 4d DS"):
        if box_dict["geometry_type"] == "polyline3d":
            poly_dict = box_dict
            for poly in poly_dict["ts_list_of_dict"]:
                ts = poly["timestamp"]
                formatted_poly = {k: v for k, v in poly.items()}
                formatted_poly["timestamp"] = ts
                formatted_poly["obj_time_varying_state"] = poly_dict["obj_time_varying_state"]
                formatted_poly["obj_track_id"] = poly_dict["obj_track_id"]
                formatted_poly["geometry_type"] = poly_dict["geometry_type"]
                formatted_poly["obj_type"] = poly_dict["obj_type"]
                formatted_poly["obj_attr"] = poly_dict["obj_attr"]
                formatted_poly["obj_type"] = poly_dict["obj_type"]
                formatted_poly["vertices"] = deepcopy(poly_dict["geometry"])
                world_T = np.eye(4)
                ego_T = np.linalg.inv(Twes[ts])
                update_poly_with_world_lidar_vertices(formatted_poly, world_T, ego_T)
                formatted_poly["velocity"] = [0, 0, 0]
                formatted_poly = deepcopy(formatted_poly)
                map_polylines_vis_dict_ts2id[ts][box_dict["obj_track_id"]] = formatted_poly
                map_polylines_vis_dict_id2ts[box_dict["obj_track_id"]][ts] = formatted_poly
        else:
            for box in box_dict["ts_list_of_dict"]:
                ts = box["timestamp"]
                formatted_box = {k: v for k, v in box.items()}
                formatted_box["obj_time_varying_state"] = box_dict["obj_time_varying_state"]
                formatted_box["obj_track_id"] = box_dict["obj_track_id"]
                formatted_box["geometry_type"] = box_dict["geometry_type"]
                formatted_box["obj_type"] = box_dict["obj_type"]
                formatted_box["timestamp"] = ts
                if box_dict["obj_time_varying_state"] == "not_varying":
                    formatted_box["obj_attr"] = box_dict["obj_attr"]
                    formatted_box["obj_type"] = box_dict["obj_type"]
                    formatted_box["geometry"] = deepcopy(box_dict["geometry"])
                    formatted_box["psr"] = translate_output_geometry_to_psr(box_dict["geometry"])
                    world_T = np.eye(4)
                    ego_T = np.linalg.inv(Twes[ts])
                    update_box_with_world_lidar_psr(formatted_box, world_T, ego_T)
                    formatted_box["velocity"] = [0, 0, 0]
                    formatted_box = deepcopy(formatted_box)
                    map_boxes_vis_dict_ts2id[ts][box_dict["obj_track_id"]] = formatted_box
                    map_boxes_vis_dict_id2ts[box_dict["obj_track_id"]][ts] = formatted_box
                elif box_dict["obj_time_varying_state"] == "varying":
                    formatted_box["obj_attr"] = box["obj_attr"]
                    formatted_box["geometry"] = deepcopy(box["geometry"])
                    formatted_box["psr"] = translate_output_geometry_to_psr(box["geometry"])
                    world_T = np.eye(4)
                    ego_T = np.linalg.inv(Twes[ts])
                    update_box_with_world_lidar_psr(formatted_box, world_T, ego_T)
                    formatted_box["velocity"] = box["velocity"]
                    formatted_box = deepcopy(formatted_box)
                    dn_boxes_vis_dict_ts2id[ts][box_dict["obj_track_id"]] = formatted_box
                    dn_boxes_vis_dict_id2ts[box_dict["obj_track_id"]][ts] = formatted_box

    return (
        dn_boxes_vis_dict_ts2id,
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_ts2id,
        map_polylines_vis_dict_id2ts,
    )


def is_visible_from_box_visiblity(vis, box_obj):
    if 'class.parking.indoor_column' in box_obj['obj_type']:
        thres = 5
    else:
        thres = 3
    return any([data > thres for cam, data in vis.items()]) 

def is_visible_from_poly_visiblity(poly):
    return any(["1" in data for cam, data in poly.items()])


def solve_ds_occlusion_sub_id(
    dn_boxes_vis_dict_ts2id,
    dn_boxes_vis_dict_id2ts,
    map_boxes_vis_dict_ts2id,
    map_boxes_vis_dict_id2ts,
    map_polylines_vis_dict_ts2id,
    map_polylines_vis_dict_id2ts,
    acc_thres=20,
):
    for track_id, box_dict in dn_boxes_vis_dict_id2ts.items():
        ts_list = sorted(box_dict.keys())
        vis_list = [is_visible_from_box_visiblity(box_dict[ts]["visibility"], box_dict[ts]) for ts in ts_list]
        acc_ts_list = []
        sub_id = 0
        st_flag = True
        for ts, visible in zip(ts_list, vis_list):
            if not visible:
                acc_ts_list += [ts]
            else:
                if not st_flag:
                    if len(acc_ts_list) >= acc_thres:
                        sub_id += 1
                    else:
                        for j in acc_ts_list:
                            box_dict[j]["sub_id"] = sub_id
                box_dict[ts]["sub_id"] = sub_id
                st_flag = False
                acc_ts_list = []

    for track_id, box_dict in map_boxes_vis_dict_id2ts.items():
        ts_list = sorted(box_dict.keys())
        vis_list = [is_visible_from_box_visiblity(box_dict[ts]["visibility"], box_dict[ts]) for ts in ts_list]
        acc_ts_list = []
        sub_id = 0
        st_flag = True
        for ts, visible in zip(ts_list, vis_list):
            if not visible:
                acc_ts_list += [ts]
            else:
                if not st_flag:
                    if len(acc_ts_list) >= acc_thres:
                        sub_id += 1
                    else:
                        for j in acc_ts_list:
                            box_dict[j]["sub_id"] = sub_id
                box_dict[ts]["sub_id"] = sub_id
                st_flag = False
                acc_ts_list = []

    for track_id, poly_dict in map_polylines_vis_dict_id2ts.items():
        ts_list = sorted(poly_dict.keys())
        vis_list = [is_visible_from_poly_visiblity(poly_dict[ts]["visibility"]) for ts in ts_list]
        acc_ts_list = []
        sub_id = 0
        st_flag = True
        for ts, visible in zip(ts_list, vis_list):
            if not visible:
                acc_ts_list += [ts]
            else:
                if not st_flag:
                    if len(acc_ts_list) >= acc_thres:
                        sub_id += 1
                    else:  # 如果没超过，之前的要补上
                        for j in acc_ts_list:
                            poly_dict[j]["sub_id"] = sub_id
                poly_dict[ts]["sub_id"] = sub_id
                st_flag = False
                acc_ts_list = []

    return (
        dn_boxes_vis_dict_ts2id,
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_ts2id,
        map_polylines_vis_dict_id2ts,
    )


def generate_4d_frame_from_4d_json(scene_root, timestamps, calib, Twes):
    (
        dn_boxes_vis_dict_ts2id,
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_ts2id,
        map_polylines_vis_dict_id2ts,
    ) = generate_DS4d_from_4dMapJson(
        op.join(scene_root, "4d_anno_infos/annos.json"), Twes
    )  # load进来转成DS4D

    print("generate finish")
    (
        dn_boxes_vis_dict_ts2id,
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_ts2id,
        map_polylines_vis_dict_id2ts,
    ) = solve_ds_occlusion_sub_id(
        dn_boxes_vis_dict_ts2id,
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_ts2id,
        map_polylines_vis_dict_id2ts,
    )  # 核心功能，generating: sub_id

    if True:
        output_json_frame_dlist = generate_4d_frame_json_data(dn_boxes_vis_dict_ts2id, map_boxes_vis_dict_ts2id, map_polylines_vis_dict_ts2id)
        for ts, frames_labels in tqdm(output_json_frame_dlist.items(), desc="generating frame json"):
            save_json_path = op.join(scene_root, f"4d_anno_infos/4d_anno_infos_frame/frames_labels/{int(ts)}.json")
            P(save_json_path).parent.mkdir(exist_ok=True, parents=True)
            write_json_from_list(frames_labels, save_json_path, format_float=True, indent=4)

def main():
    args = parser.parse_args()
    cameras = [
        "lidar1",
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
    scene_root = args.scene_root
    calib = read_cal_data(op.join(scene_root, "whole_scene/calib/calibration.yml"))
    Twes, _ = read_ego_paths(op.join(scene_root, f"whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"))
    timestamps = Timestamps.from_json(scene_root, cameras).timestamps_clean
    generate_4d_frame_from_4d_json(scene_root, timestamps, calib, Twes)


if __name__ == "__main__":
    # ---args
    main()