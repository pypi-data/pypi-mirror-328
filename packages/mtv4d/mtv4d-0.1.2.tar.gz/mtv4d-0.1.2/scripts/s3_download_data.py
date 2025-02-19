# 把所有的相关数据upload一下
import os
import os.path as op
import argparse
from pathlib import Path as P

parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default="/ssd1/data/4d/20231103_173838")  # download from s3 to local, no scene_name
parser.add_argument("--credentials_file", default="/home/yuanshiwei/.aws/credentials")  # download from s3 to local, no scene_name
parser.add_argument("--endpoint_url", default="http://192.168.23.242:8009")  # download from s3 to local, no scene_name
#  python scripts/s3_download_data.py --scene_root /tmp/1234/20230823_110018/ --endpoint_url http://192.168.22.208:9000 --credentials-file ~/.aws/credentials208
def copy_from_s3_224(src_path, dst_path, cfg_path, endpoint_url):
    os.system(f"s5cmd --credentials-file {cfg_path} --endpoint-url {endpoint_url} cp --sp {src_path} {dst_path}")
    print(f"s5cmd --credentials-file {cfg_path} --endpoint-url {endpoint_url} cp --sp {src_path} {dst_path}")


if __name__ == "__main__":
    args = parser.parse_args()

    scene_root = args.scene_root
    scene_name = P(scene_root).name
    scene_name = scene_id = P(scene_root).name 
    s3_bucket = "s3://mv-4d-annotation"
    local_root_path = scene_root

    trajectory_path = f"s3://mv-4d-annotation/AutoCollaborator/manual_annotation/baidu500/{scene_id}/whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"
    calibration_path = f"s3://mv-4d-annotation/AutoCollaborator/manual_annotation/baidu500/{scene_id}/whole_scene/calib/calibration.yml"
    objects_map_path = f"s3://mv-4d-annotation/AutoCollaborator/manual_annotation/baidu500/{scene_id}/whole_scene/objects_on_the_map/*"
    objects_frame_path = f"s3://mv-4d-annotation/AutoCollaborator/manual_annotation/baidu500/{scene_id}/whole_scene/objects_of_individual_frames/*"

    lidar_path = f"s3://mv-4d-annotation/data/MV4D_12V3L/{scene_id}/lidar/undistort_static_lidar1/*"
    im_path = f"s3://mv-4d-annotation/data/multimodel_data_baidu/{scene_id}/camera/*"
    hpr_path = f"s3://mv-4d-annotation/data/multimodel_data_baidu/{scene_id}/hidden_point_removal/*"
    hpr_lidar_path = f"s3://mv-4d-annotation/data/multimodel_data_baidu/{scene_id}/lidar/overlapped_lidar1/*"
    # lidar_box_path = f"s3://mv-4d-annotation/data/multimodel_data_baidu/{scene_id}/3d_box/3d_box_sync"
    ground_plane_path = f"s3://mv-4d-annotation/data/multimodel_data_baidu/{scene_id}/ground_plane_model/*"
    self_mask_dir = f"s3://mv-4d-annotation/data/multimodel_data_baidu/{scene_id}/self_mask/*"

    # ------- dst
    im_rel_path = "camera/"
    lidar_rel_path = "lidar/undistort_static_lidar1/"
    hpr_rel_path = "hidden_point_removal/"
    hpr_lidar_rel_path = "lidar/overlapped_lidar1/"
    # lidar_box_rel_path = "3d_box/3d_box_sync"

    trajectory_rel_path = "whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"
    calibration_rel_path = "whole_scene/calib/calibration.yml"
    objects_map_rel_path = "whole_scene/objects_on_the_map/"
    objects_frame_rel_path = "whole_scene/objects_of_individual_frames/"
    objects_ground_plane_path = "ground_plane_model/"
    self_mask_rel_path = "self_mask/"

    src_to_dst_dict = {
        trajectory_path: trajectory_rel_path,
        im_path: im_rel_path,
        lidar_path: lidar_rel_path,
        hpr_path: hpr_rel_path,
        hpr_lidar_path: hpr_lidar_rel_path,
        calibration_path: calibration_rel_path,
        objects_map_path: objects_map_rel_path,
        objects_frame_path: objects_frame_rel_path,
        ground_plane_path: objects_ground_plane_path,
        self_mask_dir: self_mask_rel_path
    }
    for src, dst in src_to_dst_dict.items():
        copy_from_s3_224(src, op.join(scene_root, dst), args.credentials_file, args.endpoint_url)

