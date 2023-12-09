
#用于程序和yolov5交互，放在这里好管理

import numpy as np
import torch
from utils.datasets import letterbox
import detect_face_boa_bak
import global_var

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_face = None
model_bin = None

def load_model():
    global model_face,model_bin
    model_face = detect_face_boa_bak.load_model(global_var.model_face_path,device)
    # model_bin = torch.hub.load('ultralytics/yolov5', 'custom', path=model_bin)

# 把拍到的数据转为yolov5输入参数
def convert_to_yolo(image):
    img = letterbox(image, new_shape=640)[0]
    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)
    return img

# 检测有无垃圾桶。修改程序，将检测结果保存到图片文件
# 处理检测结果
def detect_bin(camera_frame):
    # Load model
    model = model_bin

    # # 获取图像文件列表
    # image_files = list(Path(image_folder).glob('*.jpg'))

    # # 进行目标检测
    # results = model(image_files)

    # Get image from take_photo()
    img = convert_to_yolo(camera_frame)

    # Perform object detection
    results = model(img)

    # Save detection results to image files
    results.save()

    # 读取检测结果
    detections = []
    for img, result in zip(results.files, results.xyxy):
        for *box, conf, cls in result:
            detections.append({
                'image': img,
                'class': results.names[int(cls)],
                'confidence': conf.item(),
                'box': [x.item() for x in box]
            })
    return detections

def check_detect_bin_results(detection_results: list):
    detect_bin = 0
    for result in detection_results:
        if result['class'] == 'bin':
            detect_bin = 1
            break
    return detect_bin



def detect_face_count(frame):
    img = convert_to_yolo(frame)
    face_count = detect_face_boa_bak.detect(model_face,img,frame,device,True)
    print("face_count:" + str(face_count))
    return face_count


# def detect_bin_count(frame):
#     return check_detect_bin_results(detect_bin(frame))

def detect_bin_count(frame):
    bin_count = 1
    print("bin_count: 1")
    return bin_count
