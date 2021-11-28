#!/usr/bin/python3

import time
import json
import sys
import paho.mqtt.client as mqtt

try:
    cmd = sys.argv[1]
except:
    cmd = "play_video"

try:
    name = sys.argv[2]
except:
    name = "/home/pi/xplay/autotest/yiyezi.mp4"

try:
    value = sys.argv[3]
except:
    #value = 0
    value = str(int(time.time() + 5))
    #t = str(int(time.time() + 5))


host = "localhost"
topic = "foo/bar"

#payload = t
#payload = [{"time":t}]

payload = [{"cmd":cmd, "name":name, "value":value}]
print(value, type(payload), payload)
#print(type(json.loads(payload)), json.loads(payload))

print(int(time.time()))
#print("topic: {}, message: {}".format(topic, payload))
print("topic: {}, message: {}".format(topic, json.dumps(payload)))

client = mqtt.Client()
client.connect(host, 1883, 60)
client.publish(topic, "%s" % ( json.dumps(payload) ))

