import time
from threading import Thread, Lock
import cv2
from rubbish_room import rubbish_room
import yolov5_helpers
import numpy as np
#import aliyun_iOT_connect.run_fake as aliyun_iOT_connect

class rubbish_room_manager():
    # 在方法外面写的是静态属性
    detect_face_period = 1 #1秒检测一次有没有人
    upload_period = 10 # 10s上传一次数据

    def __init__(self,room:rubbish_room) -> None:
        self.room = room
        self.detect_timer = self.detect_face_period
        self.upload_timer = self.upload_period
        self.scheduler_thread = Thread(target=self.__scheduler)
        self.scheduler_thread.start()

    def upload_data_to_aliyun(self):
        #自己写
        bin_id = 0
        for bin in self.room.bin_list:
            bin_geo_location = bin.get_geo_location()
            bin_overflow_level = bin.get_overflow_level()
            bin_id = bin_id + 1
            print("bin_id" + str(bin_id), str(bin_geo_location), str(bin_overflow_level)+"%\n")
        pass

    def take_photo(self)->np.ndarray:
        return self.room.take_photo()
    
    def get_last_photo(self):
        return self.room.last_photo
    
    def __face_in_room_handler(self,is_face_in_room):
        # 自己完善
        if is_face_in_room:
            self.room.open_all_bin()
        else:
            if self.room.bins_cover_status:
                self.upload_data_to_aliyun()
            self.room.close_all_bin()
            
    
    # 每1s执行1次的计时器，另开一个线程执行
    def __scheduler(self):
        # 自己完善
        start_time = 0
        while True:
            start_time = time.time()
            # 1s拍一张照
            # self.save_photo(self.take_photo())
            self.take_photo()

            self.detect_timer-=1
            if self.detect_timer == 0:
                self.detect_timer = self.detect_face_period
                self.__face_in_room_handler(yolov5_helpers.detect_face_count(self.room.last_photo) > 0)

            time.sleep(1-((time.time()-start_time)%1))

    # TODO 拍摄图片，同时 修改程序，检测并删除30s前拍摄的图片，将结果输出
    def save_photo(self,frame:np.ndarray):
        # timestr = time.strftime("%Y%m%d-%H%M%S")
        # filename = "imageCapture/image_" + timestr + ".jpg"
        # cv2.imwrite(filename, frame)
        # print(filename)
        # Delete images captured more than 30 seconds ago
        # for f in os.listdir('imageCapture'):
        #     fpath = os.path.join('imageCapture', f)
        #     if os.path.getctime(fpath) < time.time() - 30:
        #         os.remove(fpath)
        #         print("Deleted:", fpath)
        # return filename
        pass
