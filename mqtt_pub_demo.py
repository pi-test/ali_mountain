#!/usr/bin/python3

import time
import paho.mqtt.client as mqtt
import json


host = "localhost"
topic = "foo/bar"

t = str(int(round(time.time(), 0)))
payload = [{"time":t}]
print(type(payload), payload)
#print(type(json.loads(payload)), json.loads(payload))

print(int(time.time()))
#print("topic: {}, message: {}".format(topic, payload))
print("topic: {}, message: {}".format(topic, json.dumps(payload)))


def on_publish(client,userdata,mid):
    #print("data published \n")
    print("on_publish, mid {}".format(mid))


client = mqtt.Client()
client.on_publish = on_publish   

client.connect(host, 1883, 60)
client.publish(topic, "%s" % ( json.dumps(payload) ), qos=0)
