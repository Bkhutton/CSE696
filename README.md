# CSE696

## 1. General Setup
Install Microsoft Visual Studio Code (VSCode)
https://code.visualstudio.com/download

Install PlatformIO (PIO) extension from the VSCode Extensions Tab

Buy the following parts (or pick your own!):
* https://www.amazon.com/DORHEA-Development-Microcontroller-NodeMCU-32S-ESP-WROOM-32/dp/B086MLNH7N?th=1
* https://www.adafruit.com/product/2651#technical-details
* https://www.amazon.com/MAX30100-Oximeters-Development-auxiliary-monitoring/dp/B08L12BJ7Q
* Any breadboard
* Spare electronics wire
* USB Micro-B to USB Type-A power and data cable

## 2. ESP32 Setup
Select 'Create New Project' button in the PlatformIO Tab on VSCode
Select the 'New Project' option in the PIO Home Tab
In the board field input 'ESP32' and select your ESP32 board
Keep 'Arduino' as the default Framework
Select 'Finish'
Clone this GitHub repository, the ESP32/src directory contains the C++ files to copy over to your project
Wire the hardware using the schematic shown below
![Circuit Diagram](https://github.com/bkhutton/CSE696/blob/master/Circuit_Diagram.png?raw=true)
Plug the USB Micro-B to USB Type-A into your PC and ESP32
Select the PlatformIO tab and select 'Upload and Monitor'. This will upload the code to the ESP32 and receive serial input from the ESP32.
Verify the ESP32 shows a connected signature to WiFi in the serial monitor. Note it will fail connecting to the MQTT Broker because it will be setup in the next step.

## Docker Compose Setup

## Delay Tolerant Gateway Setup

## InfluxDB Setup

## Grafana Setup