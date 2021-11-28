#!/usr/bin/python3

import time
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: {}".format(str(rc)))
    client.subscribe("foo/bar")

    #print("Connected flags"+str(flags)+"result code"  +str(rc)+"client1_id ")
    #client.connected_flag=True

def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    print("topic: {}, message: {}".format(msg.topic, payload))
    payload = json.loads(payload)[0]
    print(payload)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()


