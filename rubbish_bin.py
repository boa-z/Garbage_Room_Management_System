from bin_stm32 import bin_stm32

class rubbish_bin(): 
    def __init__(self,stm32:bin_stm32) -> None:
        self.stm32 = stm32 # 每个垃圾桶都配置stm32以及传感器
        self.cover_open = False #false关 True开

    def open_bin(self,force=False):
        if not self.cover_open or not force:
            self.stm32.send_open_instruction()
            self.cover_open = True

    def close_bin(self,force=False):
        if self.cover_open or not force:
            self.stm32.send_close_instruction()
            self.cover_open = False

    def get_geo_location(self):
        return self.stm32.get_geo_location()
    
    def get_overflow_level(self):
        return self.stm32.get_overflow_level()
