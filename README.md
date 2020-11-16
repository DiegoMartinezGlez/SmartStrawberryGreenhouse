# SmartStrawberryGreenhouse

## Introduction
*SmartStrawberryGreenhouse* is an IoT-GreenHouse project to frow strawberries. The main goal is to grow strawberries out of season with automations, using indoor lights and monitoring temperature and humidity to keep them into the required ranges.

## Project components
### Orchard
#### Description
Strawberries are planted in a single circular pot (40 cm. diameter), inside a custom wooden box (60x60x60 cm aprox).
#### Illumination
[XXX details] light ...
#### IoT telemetry
A raspberry 3 model b+ with raspbian strech (no desktop) with a DHT11 sensor (temperature+humidity) is used to send telemetry to ThingsBoard.
The job is scheduled with "crontab", runs each hour and calls a python script.
### IoT Server
*Thingsboard*, an open source IoT server (http://thingsboard.io/) has been configured in a Raspberry 4 (you can use also Raspberry 3 or any other computers, check ThingsBoard requirements).
## IoT devices
For this project you need at leats 1 device to make:
- Read temp/humidity and send data to IoT server
- Host IoT server
- Manage water
- Manage light
- Take orchard pics

As I said, you can configure 1 device for everything. Raspberry 3/4 should work if you don't waste resources and performance (check ThingsBoard setup for raspberry, Thingsboard will be the heaviest resource for the device).

I have used a Raspberry 4 with ThingsBoard and a Raspberry 3 for all the other things, because I had a ThingsBoard server running at home for another projects.

## How-to
You can choose what to plant and how (# of pots, light, orchard sizes, ...). But I'm going to explain how I have configured the IoT stuff: 
- Temp/humidity sensor, how to read and send to IoT server
- How to manage water (in progress)
- How to take pics (in progress)
- How to manage light

TODO: ...
