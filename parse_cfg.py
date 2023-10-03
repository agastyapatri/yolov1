import numpy as np 
import os 

def parse_config_file(path:str):
    yolo_config = {} 
    with open(path, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if lines[i][0] == "[":
            sect_name = lines[i][1:-2]
            yolo_config[sect_name] = None 
    return yolo_config
        
print(parse_config_file("yolov1.cfg"))
