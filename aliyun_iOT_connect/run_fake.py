#!/usr/bin/python3

import aliyun_iOT_connect.aliLink as aliLink
import aliyun_iOT_connect.mqttd as mqttd
import aliyun_iOT_connect.rpi as rpi
import time
import json

def send_message(ProductKey, DeviceName, DeviceSecret, POST, POST_REPLY, SET, distance, Geolocation):
    # 三元素（iot后台获取）
    ProductKey = ProductKey
    DeviceName = DeviceName
    DeviceSecret = DeviceSecret
    # topic (iot后台获取)
    POST = POST  # 上报消息到云
    POST_REPLY = POST_REPLY
    SET = SET  # 订阅云端指令

    # 消息回调（云端下发消息的回调函数）
    def on_message(client, userdata, msg):
        # print(msg.payload)
        Msg = json.loads(msg.payload)
        switch = Msg['params']['PowerLed']
        rpi.powerLed(switch)
        print(msg.payload)  # 开关值

    # 连接回调（与阿里云建立链接后的回调函数）
    def on_connect(client, userdata, flags, rc):
        pass

    # 链接信息
    Server, ClientId, userNmae, Password = aliLink.linkiot(
        DeviceName, ProductKey, DeviceSecret)

    # mqtt链接
    mqtt = mqttd.MQTT(Server, ClientId, userNmae, Password)
    mqtt.subscribe(SET)  # 订阅服务器下发消息topic
    mqtt.begin(on_message, on_connect)

    # 构建与云端模型一致的消息结构
    updateMsn = {
        "distance": distance,
        "Geolocation": Geolocation
    }
    JsonUpdataMsn = aliLink.Alink(updateMsn)
    print(JsonUpdataMsn)

    mqtt.push(POST, JsonUpdataMsn)  # 定时向阿里云IOT推送我们构建好的Alink协议数据
    return JsonUpdataMsn
