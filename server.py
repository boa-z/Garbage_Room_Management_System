# 使用 OpenCV 库来捕获来自摄像头的视频并在本地网页服务器上显示实时视频。使用 Flask 库来搭建网页服务器。
# 访问 `http://localhost:11459` 来查看实时视频。
# 使用 `cv2.VideoCapture` 类的 `set` 方法来设置视频捕获的属性。要设置视频的宽度和高度，可以分别使用 `cv2.CAP_PROP_FRAME_WIDTH` 和 `cv2.CAP_PROP_FRAME_HEIGHT` 属性。

import cv2
from flask import Flask, Response
from flask import render_template

app = Flask(__name__)

@app.route('/video')  
def video():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/')
def index():
    return render_template('index.html')

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

def generate():
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11459)
