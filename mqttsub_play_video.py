#!/usr/bin/python3

import time
import threading
import paho.mqtt.client as mqtt
import os
import json

def stop_video(name, timestamp):
    print("def stop_video")
    os.system("killall omxplayer.bin")



def play_video(name, timestamp):
    t = str(int(round(time.time(), 0)))
    print(type(t))
    print(t, timestamp)

    while True:
        t = str(int(round(time.time(), 0))).replace('"', '').rstrip()
        timestamp = str(timestamp).replace('"', '').rstrip()

        if (t == timestamp):
            print(timestamp)
            print("HELLO")
            #os.system("omxplayer --vol -2000 /home/pi/xplay/autotest/yiyezi.mp4")
            os.system("omxplayer --vol -2000 " + name)




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

    payload = json.loads(payload)[0]

    cmd = payload['cmd']
    name = payload['name']
    value = payload['value']

    print(cmd, name, value)

    if cmd == "play_video":
        t1 = threading.Thread(target=play_video, args=(name, value, ))
        t1.start()
    elif cmd == "stop_video":
        t1 = threading.Thread(target=stop_video, args=(name, value, ))
        t1.start()




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()

