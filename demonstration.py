import argparse
import json
import time
import os
import torch
import random
import utils_114 as utils
import aliyun_iOT_connect.run_fake as aliyun_run
from yolov5_face.detect_face_boa import detect as detect_face

with open('config.json') as f:
    config = json.load(f)

ProductKey = config['ProductKey']
DeviceName = config['DeviceName']
DeviceSecret = config['DeviceSecret']
POST = config['POST']
POST_REPLY = config['POST_REPLY']
SET = config['SET']
model_path_bin = config['model_path_bin']

if not os.path.exists('imageCapture'):
    os.makedirs('imageCapture')

# 开关
distance = random.randrange(0, 101)
switch = random.randrange(0, 2)
# 北斗
Geolocation = {
    "Longitude": 114,
    "Latitude": 51.4,
    "Altitude": random.randint(0, 100)
    }

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = load_model("/Users/boa/Documents/SUEP_Lab107_2023_2/2022-2023-2计算机大赛/Smart_Garbage_Room_Management_System/yolov5_face/yolov5s-face.pt",device)

# 演示各个模块
# 演示超声波
def module1():
    while True:
        print("Running module 1")
        yolov5.utils.control_32(switch)
        overflow_level, geolocation = yolov5.utils.collect_32_data()
        print(overflow_level + geolocation)
        time.sleep(1)

# 演示北斗模块(fake)
def module2():
    print("Running module 2")
    aliyun_run.send_message(ProductKey, DeviceName, DeviceSecret, POST, POST_REPLY, SET, distance, switch, Geolocation)

# 演示舵机
def module3():
    print("Running module 3")
    while True:
        switch = random.randint(0, 1)
        print(switch)
        yolov5.utils.control_32(switch)
        time.sleep(53)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run one of three modules')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_module1 = subparsers.add_parser('module1', help='module1 help')
    parser_module1.set_defaults(func=module1)

    parser_module2 = subparsers.add_parser('module2', help='module2 help')
    parser_module2.set_defaults(func=module2)

    parser_module3 = subparsers.add_parser('module3', help='module3 help')
    parser_module3.set_defaults(func=module3)

    args = parser.parse_args()
    args.func(3)