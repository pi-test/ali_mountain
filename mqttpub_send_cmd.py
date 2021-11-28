#!/usr/bin/python3

import time
import json
import paho.mqtt.client as mqtt

host = "localhost"
topic = "foo/bar"

t = str(int(time.time() + 5))
payload = t
#payload = [{"time":t}]
print(t, type(payload), payload)
#print(type(json.loads(payload)), json.loads(payload))

print(int(time.time()))
#print("t = ", t)
print("topic: {}, message: {}".format(topic, payload))
#print("topic: {}, message: {}".format(topic, json.dumps(payload)))

client = mqtt.Client()
client.connect(host, 1883, 60)
client.publish(topic, "%s" % ( json.dumps(payload) ))

