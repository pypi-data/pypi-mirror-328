# s3://mv-4d-annotation/AutoCollaborator/manual_annotation/baidu500/20230823_110018/whole_scene/
# s3://mv-4d-annotation/data/multimodel_data_baidu/20230823_110018/3d_box/3d_box_sync

import sys
import warnings

sys.path.append(".")
warnings.filterwarnings("ignore")
from mtv4d.annos_4d.reusable_4d_functions import load_and_transfer_dn_boxes_from_frame
from mtv4d.utils.geo_base import transform_pts_with_T
from mtv4d.utils.calib_base import read_ego_paths, read_cal_data
from mtv4d.utils.box_base import translate_psr_to_output_geometry, translate_psr_with_T
from mtv4d.utils.misc_base import find_path_from_ts_and_dir_path, find_path_from_ts_and_dir_path_maybe_not_find
from mtv4d.utils.io_base import read_json, write_json_from_list
from mtv4d.utils.sensors import to_camera_xy
import os.path as op
from collections import defaultdict
from copy import deepcopy
import torch
from mtv4d.utils.timestamp_base import Timestamps
from tqdm import tqdm
import argparse
import numpy as np
from pathlib import Path as P


parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default="/ssd4/data/4d/20231028_150815")

class_to_4d_obj_type = {
    103: "car",
    102: "truck",
    101: "van",
    104: "van",
    105: "van",
    106: "van",
    107: "van",
    108: "van",
    109: "van",
    201: "van",
    202: "van",
    301: "van",
}

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


def load_and_transfer_annos_from_map(manual_map_anno_dir):
    box_static_dict_id2info = {}
    map_boxes = read_json(manual_map_anno_dir)
    for i in map_boxes:
        box_static_dict_id2info[i["obj_track_id"]] = i
    return box_static_dict_id2info


def update_dn_box_with_visibility(dn_boxes_dict_ts2id, dn_boxes_dict_id2ts, vis_dy_ts2id, vis_dy_id2ts):
    for ts, frame_boxes in dn_boxes_dict_ts2id.items():
        for track_id, box in frame_boxes.items():
            box["visibility"] = vis_dy_ts2id[ts][track_id]

    for track_id, temporal_box in dn_boxes_dict_id2ts.items():
        for ts, box in temporal_box.items():
            assert "visibility" in box.keys()
            box["visibility"] = vis_dy_id2ts[track_id][ts]
    return dn_boxes_dict_ts2id, dn_boxes_dict_id2ts


def update_and_generate_DS4d_with_visibility(map_boxes, vis_dy_ts2id, timestamps):
    map_boxes_vis_dict_ts2id, map_boxes_vis_dict_id2ts = defaultdict(dict), defaultdict(dict)
    for track_id, box in map_boxes.items():
        for ts in timestamps:
            box = deepcopy(box)
            box["visibility"] = vis_dy_ts2id[ts][track_id]
            map_boxes_vis_dict_ts2id[ts][track_id] = box
            map_boxes_vis_dict_id2ts[track_id][ts] = box
    return map_boxes_vis_dict_ts2id, map_boxes_vis_dict_id2ts


# -------------------------------
# --- generate output
# -------------------------------


def generate_4d_box_dn(boxes, track_id):
    # 需要的内容
    ts = sorted(boxes.keys())[0]
    box = boxes[ts]

    # TODO: 修改成ordered_dict
    box_single_id = {
        "obj_type": box["obj_type"],
        "obj_track_id": track_id,
        "obj_time_varying_state": "varying",  # 状态&位置
        "geometry_type": "box3d",
        "ts_list_of_dict": [
            {
                "timestamp": ts,
                "obj_attr": b["obj_attr"] if "obj_attr" in b.keys() else {},
                "visibility": b["visibility"],
                "velocity": b["velocity"],
                "geometry": b["psr_world"],
            }
            for ts, b in sorted(boxes.items(), key=lambda d: d[0])
        ],
    }
    return box_single_id


def generate_4d_box_map(boxes, track_id):
    # 输入的格式和上面的内容假定一致
    # TODO: 修改成ordered_dict
    if len(list(boxes.keys())) == 0:
        return error

    box = boxes[list(boxes.keys())[0]]
    box_single_id = {
        "obj_type": box["obj_type"],
        "obj_track_id": track_id,
        "obj_time_varying_state": "not_varying",
        "geometry_type": "box3d",
        "geometry": box["psr_world"],
        "obj_attr": box["obj_attr"],
        "velocity": [0, 0, 0],
        "ts_list_of_dict": [
            {
                "timestamp": ts,
                "visibility": b["visibility"],
            }
            for ts, b in sorted(boxes.items(), key=lambda d: d[0])
        ],
    }
    return box_single_id


def generate_4d_polyline_map(polylines, track_id):
    # 输入的格式和上面的内容假定一致
    # TODO: 修改成ordered_dict, 这里有个内容是属性的变动
    if len(list(polylines.keys())) == 0:
        return error

    polyline0 = polylines[list(polylines.keys())[0]]
    polyline_single_id = {
        "obj_type": polyline0["obj_type"],
        "obj_track_id": track_id,
        "obj_time_varying_state": "not_applicable",
        "geometry_type": "polyline3d",
        "geometry": polyline0["vertices_world"],
        "obj_attr": polyline0["obj_attr"],
        "velocity": [0, 0, 0],
        "ts_list_of_dict": [
            {
                "timestamp": ts,
                "visibility": p["visibility"],
                "post_processed_attr": p["post_processed_attr"] if "post_processed_attr" in p.keys() else {},
                # 这个数据需要在转DS4d的时候进行处理
            }
            for ts, p in sorted(polylines.items(), key=lambda d: d[0])
        ],
    }
    return polyline_single_id


def generate_4d_json_data(dn_boxes_vis_dict_id2ts, map_boxes_vis_dict_id2ts, map_polylines_vis_dict_id2ts):
    output_4d_json = []

    for track_id, boxes in dn_boxes_vis_dict_id2ts.items():
        box_info = generate_4d_box_dn(boxes, track_id)
        output_4d_json.append(box_info)

    for track_id, boxes in map_boxes_vis_dict_id2ts.items():
        box_info = generate_4d_box_map(boxes, track_id)
        output_4d_json.append(box_info)

    for track_id, polylines in map_polylines_vis_dict_id2ts.items():
        polyline_info = generate_4d_polyline_map(polylines, track_id)
        output_4d_json.append(polyline_info)

    return output_4d_json



# ==================================
# === end of generate output
# ==================================


def translate_output_geometry_to_psr(box):
    x, y, z = box["pos_xyz"]
    a, b, c = box["scale_xyz"]
    rx, ry, rz = box["rot_xyz"]
    return {"position": {"x": x, "y": y, "z": z}, "scale": {"x": a, "y": b, "z": c}, "rotation": {"x": rx, "y": ry, "z": rz}}


def update_box_with_world_lidar_psr(box, world_T, ego_T):
    psr = box["psr"]
    box["psr_world"] = translate_psr_to_output_geometry(translate_psr_with_T(psr, world_T))
    box["psr_ego"] = translate_psr_to_output_geometry(translate_psr_with_T(psr, ego_T))


def update_poly_with_world_lidar_vertices(polyline, world_T, ego_T):
    vertices = polyline["vertices"]
    polyline["vertices_world"] = transform_pts_with_T(vertices, world_T).reshape(-1, 3).tolist()
    polyline["vertices_ego"] = transform_pts_with_T(vertices, ego_T).reshape(-1, 3).tolist()


def add_psr_world_and_lidar_to_dicts(dic_ts2id, Twes, src="ego"):
    assert src in ["ego", "lidar", "map"]
    for ts, box_dic in tqdm(dic_ts2id.items(), desc="box coord changing"):
        for track_id, box in box_dic.items():
            if src == "map":
                world_T = np.eye(4)
                ego_T = np.linalg.inv(Twes[ts])
            elif src == "ego":
                world_T = Twes[ts]
                ego_T = np.eye(4)
            update_box_with_world_lidar_psr(box, world_T, ego_T)


def add_psr_world_and_lidar_to_dicts_poly(dic_ts2id, Twes, src="ego"):
    assert src in ["ego", "lidar", "map"]
    for ts, poly_dic in tqdm(dic_ts2id.items(), desc="transform poly world&ego"):
        for track_id, poly in poly_dic.items():
            if src == "map":
                world_T = np.eye(4)
                ego_T = np.linalg.inv(Twes[ts])
            elif src == "ego":
                world_T = Twes[ts]
                ego_T = np.eye(4)
            update_poly_with_world_lidar_vertices(poly, world_T, ego_T)


def calculate_velocity(ts, box_dict):
    if len(box_dict.keys()) == 1:
        return [0, 0, 0]
    ts_list = np.array(sorted(box_dict.keys()))
    idx = np.where(ts_list == ts)[0][0]
    if idx == 0:
        ts1 = ts_list[idx + 1]
        ts0 = ts_list[idx]
    elif idx == len(ts_list) - 1:
        ts1 = ts_list[idx]
        ts0 = ts_list[idx - 1]
    else:
        ts1 = ts_list[idx + 1]
        ts0 = ts_list[idx - 1]
    velocity = np.array(box_dict[ts1]["psr_world"]["pos_xyz"]) - np.array(box_dict[ts0]["psr_world"]["pos_xyz"])
    v = velocity / (ts1 - ts0) * 1000  # m/s
    return v.tolist()


def add_velocity_dn_box_to_dicts(dic_ts2id, dic_id2ts):
    for track_id, box_dict in tqdm(dic_id2ts.items(), desc="add dn box velocity"):
        for ts, box in box_dict.items():
            box["velocity"] = calculate_velocity(ts, box_dict)


def add_velocity_map_box_to_dicts(dic_ts2id, dic_id2ts):
    for track_id, box_dict in dic_id2ts.items():
        for ts, box in box_dict.items():
            box["velocity"] = [0, 0, 0]



def resort_all_the_track_id(
    dn_boxes_vis_dict_id2ts,
    map_boxes_vis_dict_id2ts,
    map_polylines_vis_dict_id2ts,
    dn_boxes_vis_dict_ts2id,
    map_boxes_vis_dict_ts2id,
    map_polylines_vis_dict_ts2id,
):
    dn_boxes_vis_dict_id2ts_, map_boxes_vis_dict_id2ts_, map_polylines_vis_dict_id2ts_ = defaultdict(dict), defaultdict(dict), defaultdict(dict)
    dn_boxes_vis_dict_ts2id_, map_boxes_vis_dict_ts2id_, map_polylines_vis_dict_ts2id_ = defaultdict(dict), defaultdict(dict), defaultdict(dict)
    new_track_id = 0  # dn
    for track_id, box_dict in dn_boxes_vis_dict_id2ts.items():
        for ts, box in box_dict.items():
            box["obj_track_id"] = new_track_id
            dn_boxes_vis_dict_id2ts_[new_track_id][ts] = box
            dn_boxes_vis_dict_ts2id_[ts][new_track_id] = box
        new_track_id += 1
    new_track_id = 10000  # map box
    for track_id, box_dict in map_boxes_vis_dict_id2ts.items():
        for ts, box in box_dict.items():
            box["obj_track_id"] = new_track_id
            map_boxes_vis_dict_id2ts_[new_track_id][ts] = box
            map_boxes_vis_dict_ts2id_[ts][new_track_id] = box
        new_track_id += 1
    new_track_id = 20000  # poly
    for track_id, poly_dict in map_polylines_vis_dict_id2ts.items():
        for ts, poly in poly_dict.items():
            poly["obj_track_id"] = new_track_id
            map_polylines_vis_dict_id2ts_[new_track_id][ts] = poly
            map_polylines_vis_dict_ts2id_[ts][new_track_id] = poly
        new_track_id += 1
    return (
        dn_boxes_vis_dict_id2ts_,
        map_boxes_vis_dict_id2ts_,
        map_polylines_vis_dict_id2ts_,
        dn_boxes_vis_dict_ts2id_,
        map_boxes_vis_dict_ts2id_,
        map_polylines_vis_dict_ts2id_,
    )



def tmp_draw(timestamp, visibility, polylines_ego, sensor="camera8"):
    import cv2

    keys = sorted(polylines_ego.keys())
    vertices = [polylines_ego[k]["vertices"] for k in keys]
    visib = [visibility[k][sensor] for k in keys]
    points = np.concatenate(vertices).reshape(-1, 3)
    points = transform_pts_with_T(points, calib[sensor]["T_se"] @ np.linalg.inv(Twes[timestamp]))
    points = to_camera_xy(op.join(scene_root, "whole_scene/calib/calibration.yml"), sensor, points).astype("int")
    im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, "camera", sensor))
    im = cv2.imread(im_path)
    for i, j in zip(points, "".join(visib)):
        if int(j):
            cv2.circle(im, tuple(i), 5, (0, 0, 255), 5)
    for vis, pts in zip(visib, vertices):
        if "1" in vis:
            clr = (255, 0, 0)
        else:
            clr = (0, 255, 0)
        pts = np.array(pts).reshape(-1, 3)
        pts = transform_pts_with_T(pts, calib[sensor]["T_se"] @ np.linalg.inv(Twes[timestamp]))
        pts = to_camera_xy(op.join(scene_root, "whole_scene/calib/calibration.yml"), sensor, pts).astype("int")
        cv2.polylines(im, [pts.reshape(-1, 2)], 0, clr, 2)

    save_path = f"/tmp/12345/{sensor}/{timestamp}.jpg"
    P(save_path).parent.mkdir(exist_ok=True, parents=True)
    cv2.imwrite(save_path, im)


def get_reference_height(boxes):
    reference_boxes = [i["psr_ego"] for i in boxes.values() if i["obj_type"] == "class.parking.indoor_column"]
    if len(reference_boxes) == 0:
        return 4
    tops = np.array([b["pos_xyz"][2] + b["scale_xyz"][2] / 2 for b in reference_boxes])
    picked_heights = [i for i in tops if i < 4 and i > 2]
    if len(picked_heights) == 0:
        return 4
    reference_height = np.percentile(picked_heights, 90)
    return reference_height


def filter_other_floor_boxes(reference_height, dn_boxes, map_boxes):
    if dn_boxes is not None:
        for k, v in dn_boxes.items():
            if v["psr_ego"]["pos_xyz"][2] > reference_height:
                for sensor in v["visibility"].keys():
                    v["visibility"][sensor] = 0
    for k, v in map_boxes.items():
        if v["psr_ego"]["pos_xyz"][2] > reference_height:
            for sensor in v["visibility"].keys():
                v["visibility"][sensor] = 0


def filter_mistaken_visibility(timestamps, dn_boxes_vis_dict_ts2id, map_boxes_vis_dict_ts2id):
    reference_height = get_reference_height(map_boxes_vis_dict_ts2id[timestamps[0]])
    for ts in timestamps:
        filter_other_floor_boxes(reference_height, 
                                 dn_boxes_vis_dict_ts2id[ts] if ts in dn_boxes_vis_dict_ts2id.keys() else None, 
                                 map_boxes_vis_dict_ts2id[ts]
                                 )


def generate_labels_scene(scene_root, timestamps, Twes, calib):
    manual_map_anno_dir = op.join(scene_root, "whole_scene/objects_on_the_map")
    manual_frames_anno_dir = op.join(scene_root, "whole_scene/objects_of_individual_frames/boxes")
    if True:  # polylines
        map_polylines = read_json(op.join(manual_map_anno_dir, f"polylines/trajectory_temp_horizontal_interpolate_carline.json"))
        map_polylines = {i["obj_track_id"]: i for i in map_polylines}
        vis_poly_ts2id, vis_poly_id2ts = torch.load(op.join(scene_root, "4d_anno_infos/vis_poly.pth"))
        map_polylines_vis_dict_ts2id, map_polylines_vis_dict_id2ts = update_and_generate_DS4d_with_visibility(map_polylines, vis_poly_ts2id, timestamps)
        add_psr_world_and_lidar_to_dicts_poly(map_polylines_vis_dict_ts2id, Twes, src="map")
    else:
        map_polylines_vis_dict_ts2id, map_polylines_vis_dict_id2ts = {}, {}

    print("load poly ready")
    if True:  # boxes
        dn_boxes_dict_ts2id, dn_boxes_dict_id2ts = load_and_transfer_dn_boxes_from_frame(manual_frames_anno_dir, timestamps)
        vis_dy_ts2id, vis_dy_id2ts = torch.load(op.join(scene_root, "4d_anno_infos/vis_dnbox.pth"))
        dn_boxes_vis_dict_ts2id, dn_boxes_vis_dict_id2ts = update_dn_box_with_visibility(dn_boxes_dict_ts2id, dn_boxes_dict_id2ts, vis_dy_ts2id, vis_dy_id2ts)
        add_psr_world_and_lidar_to_dicts(dn_boxes_vis_dict_ts2id, Twes, src="ego")
        add_velocity_dn_box_to_dicts(dn_boxes_vis_dict_ts2id, dn_boxes_vis_dict_id2ts)
        print("dn ready")
        # # ----------------------------------------
        # map box
        map_boxes = load_and_transfer_annos_from_map(op.join(manual_map_anno_dir, "boxes/trajectory_temp_horizontal.json"))
        vis_map_ts2id, vis_map_id2ts = torch.load(op.join(scene_root, "4d_anno_infos/vis_mapbox.pth"))
        map_boxes_vis_dict_ts2id, map_boxes_vis_dict_id2ts = update_and_generate_DS4d_with_visibility(map_boxes, vis_map_ts2id, timestamps)
        add_psr_world_and_lidar_to_dicts(map_boxes_vis_dict_ts2id, Twes, src="map")
        add_velocity_map_box_to_dicts(map_boxes_vis_dict_ts2id, map_boxes_vis_dict_id2ts)
        print("map ready")
    else:
        dn_boxes_vis_dict_ts2id, dn_boxes_vis_dict_id2ts = {}, {}
        map_boxes_vis_dict_ts2id, map_boxes_vis_dict_id2ts = {}, {}

    if True:
        filter_mistaken_visibility(timestamps, dn_boxes_vis_dict_ts2id, map_boxes_vis_dict_ts2id)

    print("load box ready")
    # --- 上述就是我们所有数据都要维护的一个中间结果，一般是6个字典，称之为 DS4d
    (
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_id2ts,
        dn_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_ts2id,
        map_polylines_vis_dict_ts2id,
    ) = resort_all_the_track_id(
        dn_boxes_vis_dict_id2ts,
        map_boxes_vis_dict_id2ts,
        map_polylines_vis_dict_id2ts,
        dn_boxes_vis_dict_ts2id,
        map_boxes_vis_dict_ts2id,
        map_polylines_vis_dict_ts2id,
    )
    print("resort ready")
    if True:
        output_json_list = generate_4d_json_data(dn_boxes_vis_dict_id2ts, map_boxes_vis_dict_id2ts, map_polylines_vis_dict_id2ts)
        write_json_from_list(output_json_list, op.join(scene_root, "4d_anno_infos/annos.json"), format_float=True)


def main():
    cameras = [
        "camera1",
        "camera5",
        "camera8",
        "camera11",
        "camera2",
        "camera3",
        "camera4",
        "camera",
        "camera6",
        "camera7",
        "camera15",
        "camera12",
    ]

    args = parser.parse_args()
    scene_root = args.scene_root
    calib = read_cal_data(op.join(scene_root, "whole_scene/calib/calibration.yml"))
    Twes, _ = read_ego_paths(op.join(scene_root, f"whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"))
    timestamps = Timestamps.from_json(scene_root, cameras).timestamps_clean
    generate_labels_scene(scene_root, timestamps, Twes, calib)


if __name__ == "__main__":
    main()
