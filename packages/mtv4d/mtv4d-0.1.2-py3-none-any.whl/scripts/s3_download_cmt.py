# 把所有的相关数据upload一下
import os
import os.path as op
import argparse
from pathlib import Path as P

parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default="/ssd1/data/4d/20231103_173838")  # download from s3 to local, no scene_name
parser.add_argument("--credentials_file", default="/home/yuanshiwei/.aws/credentials")  # download from s3 to local, no scene_name
parser.add_argument("--endpoint_url", default="http://192.168.23.242:8009")  # download from s3 to local, no scene_name


def is_dir(path):
    # return os.path.isdir(path)
    return len(P(path).name.split(".")) == 1


def to_s3_src_path(path):
    is_dir_path = is_dir(path)
    if is_dir_path:
        if not path.endswith("/"):
            path += "/*"
    return path, is_dir_path


def to_local_dst_path(path, is_dir_path):
    if is_dir_path:
        if not path.endswith("/"):
            path = path + "/"
    return path


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

    src_paths = [f"s3://mv-4d-annotation/data/MV4D_12V3L/{scene_id}/camera/*", 
                 f"s3://mv-4d-annotation/data/MV4D_12V3L/{scene_id}/lidar/undistort_static_lidar1/*",
                 f"s3://mv-4d-annotation/data/MV4D_12V3L/{scene_id}/4d_anno_infos/*",
                 f"s3://mv-4d-annotation/data/MV4D_12V3L/{scene_id}/trajectory.txt",
                 f"s3://mv-4d-annotation/data/MV4D_12V3L/{scene_id}/calibration_center.yml",
                 ]

    dst_paths = [
            f"{scene_root}/camera/", 
            f"{scene_root}/lidar/undistort_static_lidar1/",
            f"{scene_root}/4d_anno_infos/",
            f"{scene_root}/trajectory.txt",
            f"{scene_root}/calibration_center.yml",
    ]
    src_to_dst_dict = {src: dst for src, dst in zip(src_paths, dst_paths)}
    for src, dst in src_to_dst_dict.items():
        copy_from_s3_224(src, op.join(scene_root, dst), args.credentials_file, args.endpoint_url)

    """
20231107_152423
20231031_133418
20230823_162939
20231108_153013
20231101_172858
20230831_151057
20231027_185823
20230826_102054

    """
