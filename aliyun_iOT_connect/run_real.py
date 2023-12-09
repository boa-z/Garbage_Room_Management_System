#!/usr/bin/python3

import aliLink,mqttd,rpi
import time,json
import random


# 三元素（iot后台获取）
ProductKey = 'id5cosmrou8'
DeviceName = 'dustbin_01'
DeviceSecret = "67253d45858025bbfe976d86ec16ffcc"
# topic (iot后台获取)
POST = '/sys/id5cosmrou8/dustbin_01/thing/event/property/post'  # 上报消息到云
POST_REPLY = '/sys/id5cosmrou8/dustbin_01/thing/event/property/post_reply'  
SET = '/sys/id5cosmrou8/dustbin_01/thing/service/property/set'  # 订阅云端指令

def send_message():
    # 消息回调（云端下发消息的回调函数）
    def on_message(client, userdata, msg):
        #print(msg.payload)
        Msg = json.loads(msg.payload)
        switch = Msg['params']['PowerLed']
        rpi.powerLed(switch)
        print(msg.payload)  # 开关值

    #连接回调（与阿里云建立链接后的回调函数）
    def on_connect(client, userdata, flags, rc):
        pass

    # 链接信息
    Server,ClientId,userNmae,Password = aliLink.linkiot(DeviceName,ProductKey,DeviceSecret)

    # mqtt链接
    mqtt = mqttd.MQTT(Server,ClientId,userNmae,Password)
    mqtt.subscribe(SET) # 订阅服务器下发消息topic
    mqtt.begin(on_message,on_connect)


    # 信息获取上报，每1秒钟上报一次系统参数
    while True:
        time.sleep(1)

        # 开关
        distance = 114
        switch = 514
        # 北斗
        Geolocation = {
        "Longitude": 114,
        "Latitude": 51.4,
        "Altitude": 1919
        }

        # 构建与云端模型一致的消息结构
        updateMsn = {
            "distance": distance,
            "switch": switch,
            "Geolocation": Geolocation
        }
        JsonUpdataMsn = aliLink.Alink(updateMsn)
        print(JsonUpdataMsn)

        mqtt.push(POST,JsonUpdataMsn) # 定时向阿里云IOT推送我们构建好的Alink协议数据

send_message()