import sys

sys.path.append('.')
from mtv4d.utils.io_base import read_json, write_json
import numpy as np
import open3d as o3d
import os.path as op
from pathlib import Path as P
from tqdm import tqdm
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--scene_root",  default="/ssd1/data/4d/20231028_150815")
parser.add_argument("--src_rel_path",  default="whole_scene/objects_on_the_map/polylines/trajectory_temp_horizontal.json")
parser.add_argument("--dst_rel_path",  default="whole_scene/objects_on_the_map/polylines/trajectory_temp_horizontal_interpolate_carline.json")

def interpolate_carline(polys):
    for p in polys:
        if p['obj_type'] == 'class.road_marker.lane_line' :
            if p['obj_attr']['attr.road_marker.lane_line.style'] == 'attr.road_marker.lane_line.style.solid':
                output_list = []
                pts = np.array(p['vertices']).reshape(-1, 3)
                for i, j in zip(pts[:-1], pts[1:]):
                    length = np.linalg.norm(i-j)  # 每1m插值一次。
                    split_num = round(length)
                    for idx in range(split_num):  
                        pc = idx / length
                        output_list += [pc * j + (1-pc) * i]
                output = np.concatenate(output_list+[pts[-1]])
                print(pts.shape, output.shape)
                output = output.reshape(-1).tolist()
                p['vertices'] = output
    return polys
    
def main(src_path, dst_path):
    polys = read_json(src_path)
    interpolated_polys = interpolate_carline(polys)
    write_json(interpolated_polys, dst_path)


if __name__ == "__main__":
    args = parser.parse_args()
    root_path = args.scene_root

    src_path = op.join(root_path, args.src_rel_path)
    dst_path = op.join(root_path, args.dst_rel_path)
    main(src_path, dst_path)