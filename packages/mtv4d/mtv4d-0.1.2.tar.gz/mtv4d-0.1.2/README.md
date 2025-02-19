# mtv4d

A 4d data sdk.

define a 4d data type and transform to frame-wise info.

1. scripts/generate_4d_json_clean.py 
    生成4d json
2. scripts/generate_4d_frame_clean.py
    生成4d frame
3. scripts/to_cmt_pkl.py
    生成pkl
4. scripts/draw_anno.py
    对应的4d frame 作图

python scripts/generate_4d_json_clean.py --scene_root  /ssd1/data/4d1/20230823_110018
python scripts/generate_4d_frame_clean.py --scene_root  /ssd1/data/4d1/20230823_110018
python scripts/draw_4d_data.py --scene_root  /ssd1/data/4d1/20230823_110018
python scripts/to_cmt_pkl.py --scene_root  /ssd1/data/4d1/20230823_110018