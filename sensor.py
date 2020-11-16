#!/usr/bin/env python3
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import time

THINGSBOARD_HOST = 'XXX.XXX.XXX.XXX'
ACCESS_TOKEN = 'XXX'

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))

data = {'temp': round(temperature,2), 'humidity': round(humidity,2)}
print('data: ', data)
json_data = json.dumps(data)
print('json_data: ', json_data)

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()
print('connected to thingsboard ...')
client.publish('v1/devices/me/telemetry', json_data, 1)
print('sending data ...')
time.sleep(5)
client.loop_stop()
client.disconnect()
print('disconnected')
