
import cv2

class room_camera():
    def __init__(self,camera_id):
        self.cap = cv2.VideoCapture(camera_id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

    def take_photo(self):
        frame:cv2.Mat = None
        ret, frame = self.cap.read()
        return frame