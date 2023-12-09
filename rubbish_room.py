import numpy as np
from room_camera import room_camera
from rubbish_bin import rubbish_bin
import yolov5_helpers

class rubbish_room():
    def __init__(self,camera:room_camera,name:str) -> None:
        self.name = name # 给垃圾房取个名字
        self.camera = camera
        self.last_photo:np.ndarray = None
        self.bin_list:list[rubbish_bin] = [] #删改应该不多，自己对列表操作下就行
        self.bins_cover_status = False #false关 True开

    def add_bin(self,new_bin:rubbish_bin):
        self.bin_list.append(new_bin)

    #打开所有的垃圾桶
    def open_all_bin(self,force=False): 
        if self.bins_cover_status and not force:
            return
        for bin in self.bin_list:
            bin.open_bin()
        self.bins_cover_status = True

    #关闭所有的垃圾桶
    def close_all_bin(self,force=False): 
        if not self.bins_cover_status and not force:
            return
        for bin in self.bin_list:
            bin.close_bin()
        self.bins_cover_status = False

    # 摄像头拍一张照
    def take_photo(self)->np.ndarray:
        self.last_photo = self.camera.take_photo()
        return self.last_photo

    # 判断垃圾房中有没有人，需要manager先控制摄像头拍照
    def detect_if_face_exist(self):
        return yolov5_helpers.detect_face_count(self.last_photo) > 0

    # 判断垃圾房中有没有垃圾桶，需要manager先控制摄像头拍照
    def detect_if_bin_exist(self):
        return yolov5_helpers.detect_bin_count(self.last_photo) > 0 #TODO yolov5_helpers.detect_bin_count写的是不是有问题