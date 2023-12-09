import json

with open('config.json') as f:
    config = json.load(f)

ProductKey = config['ProductKey']
DeviceName = config['DeviceName']
DeviceSecret = config['DeviceSecret']
POST = config['POST']
POST_REPLY = config['POST_REPLY']
SET = config['SET']

model_bin_path = config['model_bin_path']
model_face_path = config['model_face_path']