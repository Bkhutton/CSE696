# CSE696 Final Project
My CSE696 Final Project was designed to be a prototype delay tolerant data collection system for human spacecraft in low Earth orbit such as the International Space Station.

![Software Implementation Diagram](https://github.com/bkhutton/CSE696/blob/master/Software_Implementation_Diagram.png?raw=true)

## 1. General Setup
### 1.1 Install the IDE and Extensions
Install Microsoft Visual Studio Code (VSCode)<br />
https://code.visualstudio.com/download

Install PlatformIO (PIO) extension from the VSCode Extensions Tab<br />

### 1.2 Buy the necessary hardware
Buy the following parts (or pick your own!):<br />
* https://www.amazon.com/DORHEA-Development-Microcontroller-NodeMCU-32S-ESP-WROOM-32/dp/B086MLNH7N?th=1
* https://www.adafruit.com/product/2651#technical-details
* https://www.amazon.com/MAX30100-Oximeters-Development-auxiliary-monitoring/dp/B08L12BJ7Q
* Any breadboard
* Spare electronics wire
* USB Micro-B to USB Type-A power and data cable

### 1.3 Setup the server
Create a virtual machine using your favorite VM software (i.e. VirtualBox, QEMU, VMWare, etc.) with Debian. I used Bulleyes version for this project on my home server rather than using a VM, but either will work.<br />
Install Docker for Debian on the VM<br />
https://docs.docker.com/engine/install/debian/<br />
Install the Docker Compse Plugin on the VM<br />
https://docs.docker.com/compose/install/linux/<br />

## 2. Docker Compose Setup
Clone the GitHub repository to the server under the desired user's home directory<br />
Unpack all files under _Docker_ to the desired location<br />
Run the command `docker compose up -d` to start all the containers. This will setup the MQTT Broker, InfluxDB, and Grafana.<br />

## 3. Delay Tolerant Gateway Setup
Install screen with the `sudo apt-get install screen` command<br />
Install Python if needed<br />
Unpack the _dtngw_ folder into the desired dirctory<br />
Create a new screen, `screen -S dtngw`<br />
Create a virtual environment, `python -m venv [venv name]`<br />
Input `source [venv name]/activate` to activate the virtual environment<br />
Install necessary libraries, `pip install -r requirements.txt`<br />
Start DTNGW, `python dtngw.py`<br />
Verify Connected exit code = 0 and data is outputting to the terminal<br />
Exit Screen (CTRL + A + D)<br />

## 4. ESP32 Setup
Select _Create New Project_ button in the PlatformIO Tab on VSCode<br />
Select the _New Project_ option in the PIO Home Tab<br />
In the board field input _ESP32_ and select your ESP32 board<br />
Keep _Arduino_ as the default Framework<br />
Select _Finish_<br />
Clone this GitHub repository, the ESP32/src directory contains the C++ files to copy over to your project<br />
Create a _wifi_secrets.h_ header fil under the _include_ directory<br />
Define two constants `SECRET_SSID` with your WiFi SSID name and `SECRET_PASS` with your WiFi password<br />
In _src/MQTT.cpp_ edit the `broker` variable to be the hostname ir IP address of the server<br />
Wire the hardware using the schematic shown below<br />
![Circuit Diagram](https://github.com/bkhutton/CSE696/blob/master/Circuit_Diagram.png?raw=true)
Plug the USB Micro-B to USB Type-A into your PC and ESP32<br />
Select the PlatformIO tab and select _Upload and Monitor_. This will upload the code to the ESP32 and receive serial input from the ESP32.<br />
Verify the ESP32 shows a connected signature to WiFi in the serial monitor. Note it will fail connecting to the MQTT Broker because it will be setup in the next step.