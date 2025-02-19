# 把所有的相关数据upload一下
import os
import os.path as op
import argparse
from pathlib import Path as P

parser = argparse.ArgumentParser()
parser.add_argument("--scene_root", default='/ssd1/data/4d/20231103_173838')  # must not on s3
parser.add_argument("--s3_root", default="s3://mv-4d-annotation/data/MV4D_12V3L")  # must on s3
parser.add_argument("--credentials_file", default="/home/yuanshiwei/.aws/credentials")  
parser.add_argument("--endpoint_url", default="http://192.168.23.242:8009")  

def is_dir(path):
    return os.path.isdir(path)


def to_s3_src_path(path):
    is_dir_path = is_dir(path)
    if is_dir_path:
        if not path.endswith("/"):
            path += "/"
    return path, is_dir_path


def to_s3_dst_path(path, is_dir_path):
    if is_dir_path:
        if not path.endswith("/"):
            path = path + "/"
    return path


def copy_to_s3(src_root, dst_root, rel_path, credential_file, endpoint_url):
    src_path, is_dir_path = to_s3_src_path(op.join(src_root, rel_path))
    dst_path = to_s3_dst_path(op.join(dst_root, rel_path), is_dir_path)
    os.system(f"s5cmd --credentials-file {credential_file} --endpoint-url {endpoint_url} cp --sp {src_path} {dst_path}")


if __name__ == "__main__":
    args = parser.parse_args()

    # scene_name = "20230823_110018"
    s3_bucket = "s3://mv-4d-annotation"
    s3_root = args.s3_root  
    scene_root = args.scene_root
    scene_name = P(scene_root).name
    s3_scene_root = f"{s3_root}/{scene_name}"

    
    im_rel_path = "camera"
    lidar_rel_path = "lidar/undistort_static_lidar1"
    trajectory_rel_path = "whole_scene/ego-trajectory/trajectory_temp_horizontal.txt"
    calibration_rel_path = "whole_scene/calib/calibration.yml"
    mtv4d_label_rel_path = "4d_anno_infos"

    rel_path_list = [
        # im_rel_path,
        # lidar_rel_path,
        # trajectory_rel_path,
        # calibration_rel_path,
        mtv4d_label_rel_path,
    ]
    for rel_path in rel_path_list:
        copy_to_s3(scene_root, s3_scene_root, rel_path, args.credentials_file, args.endpoint_url)