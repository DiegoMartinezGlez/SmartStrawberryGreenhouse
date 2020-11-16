# SmartStrawberryGreenhouse

## Introduction
*SmartStrawberryGreenhouse* is an IoT-GreenHouse project to frow strawberries. The main goal is to grow strawberries out of season with automations, using indoor lights and monitoring temperature and humidity to keep them into the required ranges.

## Project components

### Orchard
Strawberries are planted in a sigle circular pot (diameter 40 cm), inside a custom wooden box (60x60x60 cm aprox).

### Orchard automations
#### Illumination
[XXX details] light ...
#### IoT telemetry
A raspberry 3 model b+ with raspbian strech (no desktop) with a DHT11 sensor (temperature+humidity) is used to send telemetry to ThingsBoard.
The job is scheduled with "crontab", runs each hour and calls a python script.

TODO: python script details

### IoT Server
I have configured a Thingsboard server in a Raspberry 4

