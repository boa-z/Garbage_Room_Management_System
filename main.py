import json
import time
import os
import torch
import random
# import utils_114 as utils
import aliyun_iOT_connect.run_fake as aliyun_run
# from yolov5_face.detect_face_boa import detect as detect_face
from rubbish_bin import rubbish_bin
from bin_stm32 import bin_stm32
from rubbish_room import rubbish_room
from room_camera import room_camera
from rubbish_room_manager import rubbish_room_manager
import global_var
import yolov5_helpers

if not os.path.exists('imageCapture'):
    os.makedirs('imageCapture')

yolov5_helpers.load_model()
camera = room_camera(0)
rubbish_room1 = rubbish_room(camera, "rubbish_room1")
rubbish_bin1_stm32 = bin_stm32(None)
rubbish_bin1 = rubbish_bin(rubbish_bin1_stm32)
rubbish_bin2_stm32 = bin_stm32(None)
rubbish_bin2 = rubbish_bin(rubbish_bin2_stm32)
rubbish_room1.add_bin(rubbish_bin1)
rubbish_room1.add_bin(rubbish_bin2)
rubbish_room_manager1 = rubbish_room_manager(rubbish_room1)


def main():
    pass

if __name__ == '__main__':
    main()