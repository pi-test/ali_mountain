#!/usr/bin/python3

import time
import threading
import paho.mqtt.client as mqtt
import os
import json

def play_video(timestamp):
    #print(type(timestamp))
    #t = json.loads(timestamp)
    print(timestamp)
    #t = json.loads(timestamp)
   
    print(type(timestamp))
    t = str(int(round(time.time(), 0)))
    print(type(t))
    print(t, timestamp)

    while True:
        t = str(int(round(time.time(), 0))).replace('"', '').rstrip()
        timestamp = str(timestamp).replace('"', '').rstrip()
        #print(t, timestamp)
        if (t == timestamp):
            print(timestamp)
            print("HELLO")
            #time.sleep(1)
            os.system("omxplayer --vol -2000 /home/pi/xplay/autotest/yiyezi.mp4")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: {}".format(str(rc)))
    client.subscribe("foo/bar")

def on_message(client, userdata, msg):
    #payload = str(msg.payload).decode('utf-8')
    #payload = str(msg.payload)
    #payload = [{d,"value":[humd, temp], "time":t}]
    #print("topic: {}, message: {}".format(msg.topic, payload))
    #t1 = threading.Thread(target=play_video, args=(payload,))
    payload = str(msg.payload.decode("utf-8"))
    #print(type(payload))
    #print(payload)
    #print("topic: {}, message: {}".format(msg.topic, str(msg.payload)))
    print("topic: {}, message: {}".format(msg.topic, payload))
    t1 = threading.Thread(target=play_video, args=(payload,))
    t1.start()



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()

