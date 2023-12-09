import serial
import time
import random
import os
import torch
from pathlib import Path
import cv2
import numpy as np
from room_camera import my_camera


# 还剩个函数不知道干啥的就放这了


# 检测指定目录下有没有新文件


def check_new_file():
    path_to_watch = "imageCapture"
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while True:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
            print("New file detected:", added[0])
            os.system("run.sh")
        else:
            print("No new file")
        before = after



# 拍摄图片，同时 修改程序，检测并删除30s前拍摄的图片，将结果输出


# 拍照


# while True:
#     cv2.imshow('result', take_photo()[0])
#     k = cv2.waitKey(1)
#     time.sleep(0.125)