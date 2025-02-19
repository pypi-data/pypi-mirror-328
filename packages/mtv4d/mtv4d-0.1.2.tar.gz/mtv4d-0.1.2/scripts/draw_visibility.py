# from tkinter import E
from functools import reduce
from itertools import accumulate
import sys
from pyrsistent import b

sys.path.append(".")
import numpy as np
from tqdm import tqdm
from mtv4d.utils.box_base import to_corners_9, transform_output_geometry_to_array, transform_psr_to_array
from mtv4d.utils.calib_base import read_cal_data, read_ego_paths
from mtv4d.utils.draw_base import draw_boxes, draw_points_to_cams
from mtv4d.utils.geo_base import transform_pts_with_T
from mtv4d.utils.io_base import read_json
from mtv4d.utils.misc_base import Time, find_path_from_ts_and_dir_path, mp_pool
from pathlib import Path as P
import os.path as op
import cv2
import matplotlib.pyplot as plt
from mtv4d.utils.sensors import to_camera_xy
from mtv4d.utils.timestamp_base import Timestamps

tim = Time()


def split_points_with_nums(points, num_list):
    output = []
    for i in num_list:
        poly, points = points[:i], points[i:]
        output.append(poly)
    return output


def func_4d_frame(data):
    scene_root, path, calib, cameras = data
    info = read_json(path)
    timestamp = float(P(path).stem)
    boxes, boxes_obj, polys, visb, visp = [], [], [], [], []
    # return
    poly_ids, box_type_list = [], []
    for i in info:
        geometry = i["geometry"]
        visibility = i["visibility"]
        obj_type = i["obj_type"]
        obj_track_id = i["obj_track_id"]
        geometry_type = i["geometry_type"]
        if geometry_type == "box3d":
            # if any([v > 1 for k, v in visibility.items() if 'camera' in k]):
            # if obj_type in ['class.traffic_facility.speed_bump',
            #             'class.road_marker.arrow',
            #             'class.parking.wheel_stopper',
            #             'class.parking.text_icon',
            #             'class.parking.parking_lock',
            #             'class.road_marker.text',
            #             'class.parking.indoor_column',
            #             ]: continue
            # if 'car' not in obj_type: continue
            # if obj_track_id!='10025_0': continue
            boxes.append(to_corners_9(transform_output_geometry_to_array(geometry)))
            visb.append(visibility)
            box_type_list.append(obj_track_id)
        elif geometry_type == "polyline3d":
            # if obj_type == 'class.road_marker.lane_line' :
            # if obj_type == 'class.road_marker.lane_line' :
            if obj_track_id == "20049_0":
                print(i["visibility"])
            # if obj_type == 'class.parking.parking_slot' :
            if True:
                polys.append(geometry)  # n*3
                poly_ids.append(obj_track_id)
                visp.append(i["visibility"])
    if len(boxes) > 0:
        # mask = [any([i > 4 for i in v.values()]) if 'indoor_column' in b['obj_type'] else any(v.values()) for b, v in zip(info, visb)]
        # mask = [any([i > 4 for i in v.values()]) if 'indoor_column' in b['obj_type'] else any(v.values()) for b, v in zip(info, visb)]
        # mask = [any(v.values()) for b, v in zip(info, visb)]
        mask = [max(v.values()) > 3 for b, v in zip(info, visb)]  # 原始版本不能删除
        # if sum(mask) ==0:
        #     return
        boxes = [b for b, m in zip(boxes, mask) if m]
        visb = [b for b, m in zip(visb, mask) if m]
        box_type_list = [b for b, m in zip(box_type_list, mask) if m]

        for cam in cameras:
            im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, f"camera/{cam}"))
            im = cv2.imread(im_path)
            calib_path = op.join(scene_root, "calibration_center.yml")
            # im = draw_img(im, cam, calib[cam]["T_se"], calib_path, boxes=boxes, polylines=None)
            im = draw_img(im, cam, calib[cam]["T_se"], calib_path, boxes=boxes, box_vis=None, polylines=polys, poly_vis=visp, poly_ids=poly_ids)
            # save_path = f"/tmp/1234/20231107_123645/{cam}/{timestamp}.jpg"
            save_path = f"/tmp/1234/20231103_173838/camera_only/{cam}/{timestamp}.jpg"
            P(save_path).parent.mkdir(exist_ok=True, parents=True)
            cv2.imwrite(save_path, im)


def find_dict_from_dict_list(timestamp, dl):
    for d in dl:
        if d["timestamp"] == timestamp:
            return d


def func_4d_json(data):
    scene_root, timestamp, calib, cameras, infos, Twe = data
    boxes, polys, visb, visp = [], [], [], []
    for i in infos:
        if i["geometry_type"] == "box3d":
            if i["obj_time_varying_state"] == "varying":
                b = find_dict_from_dict_list(timestamp, i["ts_list_of_dict"])
                if b is not None:
                    boxes.append(b["geometry"])
                    visb.append(b["visibility"])
            else:
                boxes.append(i["geometry"])
                visb.append(find_dict_from_dict_list(timestamp, i["ts_list_of_dict"])["visibility"])
        else:
            polys.append(i["geometry"])
            visp.append(find_dict_from_dict_list(timestamp, i["ts_list_of_dict"])["visibility"])
    tim.tic()
    if len(boxes) > 0:
        tim.tic()
        boxes_filtered = [b for b, v in zip(boxes, visb) if any(v.values())]  # 只要有一个模态可以被看到就是一个正样本。
        boxes_cam = [to_corners_9(transform_output_geometry_to_array(b)) for b in boxes_filtered]
        for cam in cameras:
            if len(boxes_cam) > 0:
                im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, f"camera/{cam}"))
                im = cv2.imread(im_path)
                calib_path = op.join(scene_root, "whole_scene/calib/calibration.yml")
                tim.tic()
                im = draw_img(im, cam, calib[cam]["T_se"] @ np.linalg.inv(Twe), calib_path, boxes=boxes_cam, polylines=None, poly_vis=visp)
                save_path = f"/tmp/1234/3/{cam}/{timestamp}.jpg"
                P(save_path).parent.mkdir(exist_ok=True, parents=True)
                cv2.imwrite(save_path, im)


def draw_img(im, cam, T_cp, calib_path, boxes=None, box_vis=None, polylines=None, poly_vis=None, poly_ids=None):
    if boxes is not None:
        points = transform_pts_with_T(np.concatenate(boxes).reshape(-1, 3), T_cp)
        mask_by_camera = [(i[:, 2] > 0).any() for i in points.reshape(-1, 8, 3)]
        if sum(mask_by_camera) > 0:
            points = np.concatenate([i for i in points.reshape(-1, 8, 3) if (i[:, 2] > 0).any()]).reshape(-1, 3)
            box2d = to_camera_xy(calib_path, cam, points)
            draw_boxes(im, box2d, [i for i, j in enumerate(mask_by_camera) if j])
    if polylines is not None:
        points = transform_pts_with_T(np.concatenate(polylines).reshape(-1, 3), T_cp)
        poly2d = to_camera_xy(calib_path, cam, points)
        for i, j in zip(split_points_with_nums(poly2d, [len(poly) for poly in polylines]), poly_ids):
            i = i.astype("int")
            cv2.polylines(im, [i.reshape(-1, 2)], False, (0, 255, 0), 2)
            cv2.putText(im, str(j), (i[0, 0], i[0, 1]), 1, 1, (0, 0, 244))
        if poly_vis is not None:
            # for i, j in zip(poly2d, "".join([v[cam] for v in poly_vis])):
            # def reduce_or(bool_list):
            #     output = [any([bool(bool_list[c][i]) for c in ['camera1', 'camera5', 'camera8', 'camera11']]) for i in range(len(bool_list['camera1']))]
            #     if len(output) != sum(output):
            #         print(len(output), sum(output))
            #     return ''.join(['1' if i else '0' for i in output])
            poly_vis_list = ["".join([v[c] for v in poly_vis]) for c in cameras]
            poly_vis_all = [any(p[i] == "1" for p in poly_vis_list) for i in range(len(poly_vis_list[0]))]
            poly_vis_all = "".join(["1" if i else "0" for i in poly_vis_all])
            # print('---', cam, poly_vis_all)
            # print('camera1', "".join([v['camera1'] for v in poly_vis]))
            # print('camera5', "".join([v['camera5'] for v in poly_vis]))
            # print('camera8', "".join([v['camera8'] for v in poly_vis]))
            # print('camera11', "".join([v['camera11'] for v in poly_vis]))
            # for i, j in zip(poly2d, "".join([v[cam] for v in poly_vis])):
            for i, j in zip(poly2d, poly_vis_all):
                if j == "1":
                    cv2.circle(im, (int(i[0]), int(i[1])), 5, (0, 128, 255), -1)
    return im


def func_visibility(data):
    scene_root, timestamp, boxes, polylines, calib, cameras, infos, Twe, vis = data
    # path = op.join(scene_root, f'whole_scene/objects_of_individual_frames/boxes/{timestamp}.json')
    # dn_boxes = read_json(path)  if P(path).exists() else []
    # boxes = boxes + dn_boxes
    vis_dnbox, vis_mapbox, vis_poly = vis
    # boxes, polys, visb, visp = [], [], [], []
    tim.tic()
    boxes_filtered = boxes
    visb = vis_mapbox

    def find_ori_id_by_mask_id(ori_list, mask, idx):
        a = np.cumsum(np.array(mask))
        new_id = np.where(a == idx)[0]
        return ori_list[new_id]

    if boxes is not None and len(boxes) > 0:
        tim.tic()
        mask_by_visibility = [any(v.values()) for b, (k, v) in zip(boxes, visb.items())]  # 只要有一个模态可以被看到就是一个正样本。
        boxes_filtered = [b for b, v in zip(boxes, mask_by_visibility) if v]
        if len(boxes_filtered) > 0:
            visb = {k: v for (k, v), m in zip(visb.items(), mask_by_visibility) if m}
            boxes_cam = [to_corners_9(transform_psr_to_array(b["psr"])) for b in boxes_filtered]
            for cam in cameras:
                T_cp = calib[cam]["T_se"] @ np.linalg.inv(Twe)
                points = transform_pts_with_T(np.concatenate(boxes_cam).reshape(-1, 3), T_cp)
                mask_by_camera = [(i[:, 2] > 0).any() for i in points.reshape(-1, 8, 3)]  # points 应该是39的倍数，但数量不对
                mask_all = np.array(mask_by_visibility, dtype="bool")  # vis的可见框，应为39个。
                mask_all[mask_all] = mask_by_camera
                mask_all[:] = 1
                boxes_cam_draw = [to_corners_9(transform_psr_to_array(b["psr"])) for b, m in zip(boxes, mask_all) if m]  # 这里有个bug

                if mask_all.sum() > 0:
                    im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, f"camera/{cam}"))
                    im = cv2.imread(im_path)
                    calib_path = op.join(scene_root, "whole_scene/calib/calibration.yml")
                    tim.tic()
                    # words = [(idx, b['obj_track_id']) for idx, (i,b) in enumerate(zip(mask_all, boxes) ) if i]
                    im = draw_img_with_mask(im, cam, calib[cam]["T_se"] @ np.linalg.inv(Twe), calib_path, boxes=boxes_cam_draw, polylines=None, mask=mask_all)
                    save_path = f"/tmp/1234/none/{cam}/9_{timestamp}.jpg"
                    P(save_path).parent.mkdir(exist_ok=True, parents=True)
                    cv2.imwrite(save_path, im)
    return
    if polylines is not None and len(polylines) > 0:

        def split_points(points, polyline_pts_list):
            indices = [0] + list(accumulate(map(int, [len(i) for i in polyline_pts_list])))
            return [points[i:j] for i, j in zip(indices[:-1], indices[1:])]

        # polylines = [i for i in polylines if i['obj_track_id'] == 455]
        polyline_pts_list_ori = [np.array(poly["vertices"]).reshape(-1, 3) for poly in polylines]
        mask_by_visibility_list = [vis_poly[poly["obj_track_id"]] for poly in polylines]
        # # 1. 被墙遮挡: inst & pt; 我感觉逻辑过于复杂了
        mask_by_visibility_instance = [any([int(i) for i in v.values()]) for v in mask_by_visibility_list]  # 只要有一个模态可以被看到就是一个正样本。

        polyline_pts_list_filtered = [i for i, j in zip(polyline_pts_list_ori, mask_by_visibility_instance) if j]
        mask_by_visibility_list_filtered = [i for i, j in zip(mask_by_visibility_list, mask_by_visibility_instance) if j]

        mask_by_visibility_filtered = (
            np.concatenate([[sum([int(j[i]) for j in v.values()]) for i in range(len(v["lidar1"]))] for v in mask_by_visibility_list_filtered]) > 0
        )  # 只要有一个模态可以被看到就是一个正样本。

        # polyline_pts_list_filtered = [i for i, v in zip(polyline_pts_list, mask_by_visibility_instance) if v]
        # mask_by_visibility_list_filtered = [i for i, v in zip(mask_by_visibility_list, mask_by_visibility_instance) if v]
        for cam in cameras:
            T_cp = calib[cam]["T_se"] @ np.linalg.inv(Twe)
            points = transform_pts_with_T(np.concatenate(polyline_pts_list_filtered).reshape(-1, 3), T_cp)  # world -> cam
            mask_pt_by_camera = points.reshape(-1, 3)[:, 2] > 0  # 2. 没有出现在镜头里。
            mask_pt_all = np.array(mask_by_visibility_filtered, dtype="bool")  # 所有的点
            mask_pt_all = mask_pt_all * mask_pt_by_camera
            if mask_pt_all.sum() > 0:
                im_path = find_path_from_ts_and_dir_path(timestamp, op.join(scene_root, f"camera/{cam}"))
                im = cv2.imread(im_path)
                calib_path = op.join(scene_root, "whole_scene/calib/calibration.yml")
                tim.tic()
                points = to_camera_xy(calib_path, cam, points)
                draw_poly_with_mask(im, split_points(points, polyline_pts_list_filtered), split_points(mask_pt_all, polyline_pts_list_filtered))
                save_path = f"/tmp/1234/polylines/{cam}/1_{timestamp}.jpg"
                P(save_path).parent.mkdir(exist_ok=True, parents=True)
                cv2.imwrite(save_path, im)


def draw_poly_with_mask(im, point_list, mask_list):
    for idx, (pt, mask) in enumerate(zip(point_list, mask_list)):
        pt = pt.astype("int").reshape(-1, 2)
        # if len(pt) !=4: continue
        cv2.polylines(im, [pt], 2, (0, 255, 0), 2)
        cv2.putText(im, str(idx), tuple(pt[0]), 2, 2, (0, 255, 0), 2)
        for p, m in zip(pt, mask):
            clr = (128, 0, 0) if m else (0, 0, 128)
            cv2.circle(im, tuple(p), 10, clr, 10)


def draw_img_with_mask(im, cam, T_cp, calib_path, boxes=None, polylines=None, mask=None):
    if len(boxes) > 0:
        points = transform_pts_with_T(np.concatenate(boxes).reshape(-1, 3), T_cp)
        points = np.concatenate([i for i in points.reshape(-1, 8, 3) if (i[:, 2] > 0).any()]).reshape(-1, 3)
        box2d = to_camera_xy(calib_path, cam, points)
        draw_boxes(im, box2d, [i for i, j in enumerate(mask) if j])
    return im


if __name__ == "__main__":

    cameras = [
        "camera6",
        "camera8",
        "camera1",
        "camera5",
        "camera11",
        "camera2",
        "camera3",
        "camera4",
        "camera7",
        "camera15",
        "camera12",
    ]

    import torch

    def main_4d_frame(scene_root):

        # scene_root = "/ssd1/data/4d/20230823_110018"
        paths = sorted(P(op.join(scene_root, "4d_anno_infos/4d_anno_infos_frame/frames_labels")).glob("*.json"))
        # if not P(op.join(scene_root, "whole_scene/calib/calibration.yml")).exists():
        calib_path =  op.join(scene_root, "calibration_center.yml")
        calib = read_cal_data(calib_path)
        # paths = [i for i in paths if '1698477211164' in str(i)]
        data = [(scene_root, i, calib, cameras) for i in paths if '1698476271964' in str(i)]

        # for i in tqdm(data[397:399]):
        # for i in tqdm(data):
        #     # if '1698476899464' in P(i[1]).stem:
        #     func_4d_frame(i)  # 先看看为什么两者算出来的点的内容是不一样的，主要看看原因是什么，总不会是一个用的hpr，一个用的原图吧。
        #         # exit()
        mp_pool(func_4d_frame, data)

    def main_4d_json(scene_root):
        # scene_root = "/ssd1/data/4d/20230823_110018"
        tim.tic()
        # infos = read_json(op.join(scene_root, "4d_anno_infos/annos_test.json"))
        infos = read_json(op.join(scene_root, "4d_anno_infos/annos.json"))
        tim.toc()
        Twes, _ = read_ego_paths(op.join(scene_root, f"whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"))
        calib = read_cal_data(op.join(scene_root, "whole_scene/calib/calibration.yml"))
        timestamps = Timestamps.from_json(scene_root, cameras).timestamps_clean
        data = [(scene_root, ts, calib, cameras, infos, Twes[ts]) for ts in timestamps]
        # mp_pool(func_4d_json, data)
        for i in tqdm(data):
            func_4d_json(i)

    def main_data_visibility(scene_root):
        # scene_root = "/ssd1/data/4d/20230823_110018"
        infos = read_json(op.join(scene_root, "4d_anno_infos/annos.json"))
        vis_dnbox = torch.load(op.join(scene_root, "4d_anno_infos/vis_dnbox.pth"))[0]
        vis_mapbox = torch.load(op.join(scene_root, "4d_anno_infos/vis_mapbox.pth"))[0]
        # # vis_mapbox = torch.load(op.join(scene_root, "4d_anno_infos/vis_mapbox.pth"))[0]
        vis_poly = torch.load(op.join(scene_root, "4d_anno_infos/vis_poly.pth"))[0]
        Twes, _ = read_ego_paths(op.join(scene_root, f"whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"))
        calib = read_cal_data(op.join(scene_root, "whole_scene/calib/calibration.yml"))
        # timestamps = Timestamps.from_json(scene_root, cameras).timestamps_clean
        timestamps = [1698476271964]
        # timestamps = [1698477211164.]
        boxes = read_json(op.join(scene_root, "whole_scene/objects_on_the_map/boxes/trajectory_temp_horizontal.json"))
        polylines = read_json(op.join(scene_root, "whole_scene/objects_on_the_map/polylines/trajectory_temp_horizontal.json"))
        # dn_boxes = read_json(op.join(scene_root, 'whole_scene/objects_of_individual_frames/polylines/trajectory_temp_horizontal.json'))
        # data = [(scene_root, ts, boxes, polylines, calib, cameras, infos, Twes[ts], (vis_dnbox[ts], vis_mapbox[ts], vis_poly[ts])) for ts in timestamps]
        data = [(scene_root, ts, boxes, polylines, calib, cameras, infos, Twes[ts], (vis_dnbox[ts], vis_mapbox[ts], vis_poly[ts])) for ts in timestamps]
        # mp_pool(func_4d_json, data)
        for i in tqdm(data):
            func_visibility(i)

    # scene_root = "/ssd1/data/4d/20230831_151057"
    # scene_root = "/ssd1/data/4d/20230826_102054"
    # scene_root = "/ssd1/data/4d/20230823_110018"
    scene_root = "/ssd1/data/4d/20231028_145730"
    # scene_root = "/ssd1/data/4d/20231107_123645"
    # main_4d_json(scene_root)
    # main_4d_frame(scene_root)
    main_data_visibility(scene_root)
