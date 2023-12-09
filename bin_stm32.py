import serial
import numbers
import random
import time
from threading import Thread,Lock


class bin_stm32():
    def __init__(self,serial) -> None:
        self.ser = serial #serial.Serial("/dev/ttyUSB0", 115200)
        self.last_geo_location = None
        self.last_overflow_level = None

        # self.log_watcher = Thread(target=self.__stm32_watcher_thread)
        # self.intstruction_watcher = Thread(target=self.__stm32_data_sender)
        # self.log_watcher.start()
        # self.intstruction_watcher.start()

        self.instruction_buffer = [] # 字符串=指令，数字=需要等待的时间 ['a', 1, 'b','5','c','d']代表a发送1s后发送b，再等待5s依次发送c和d

        self.write_lock = Lock()
        self.is_instruction_buffer_empty_lock = Lock()
        self.send_instruction_lock = Lock()
    
    
    def get_geo_location(self):
        last_geo_location = {
                "Longitude": random.uniform(121.87165109518433, 121.91165109518433), # 121.89165109518433
                "Latitude": random.uniform(30.88193593657738, 30.92193593657738), # 30.90193593657738
                "Altitude": random.randint(11.0, 12.0)
            }
        return last_geo_location
    
    def get_overflow_level(self):
        distance = random.randint(45, 55)
        if distance == 0:
            last_overflow_level = 100
        elif distance >= 100:
            last_overflow_level = 0
        else:
            last_overflow_level = 100 - distance
        return last_overflow_level
    

    # 只是发送信号，具体逻辑在rubbish_bin中实现！不会阻塞
    def send_open_instruction(self):
        print("bin open")
        pass
    
    # 只是发送信号，具体逻辑在rubbish_bin中实现！不会阻塞
    def send_close_instruction(self):
        print("bin close")
        pass
