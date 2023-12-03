# CSE696 Final Project
My CSE696 Final Project was designed to be a prototype delay tolerant data collection system for human spacecraft in low Earth orbit such as the International Space Station.

![Software Implementation Diagram](https://github.com/bkhutton/CSE696/blob/master/Software_Implementation_Diagram.png?raw=true)

## 1. General Setup
### 1.1 Install the IDE and Extensions
Install Microsoft Visual Studio Code (VSCode)
https://code.visualstudio.com/download

Install PlatformIO (PIO) extension from the VSCode Extensions Tab

### 1.2 Buy the necessary hardware
Buy the following parts (or pick your own!):
* https://www.amazon.com/DORHEA-Development-Microcontroller-NodeMCU-32S-ESP-WROOM-32/dp/B086MLNH7N?th=1
* https://www.adafruit.com/product/2651#technical-details
* https://www.amazon.com/MAX30100-Oximeters-Development-auxiliary-monitoring/dp/B08L12BJ7Q
* Any breadboard
* Spare electronics wire
* USB Micro-B to USB Type-A power and data cable

### 1.3 Setup the server
Create a virtual machine using your favorite VM software (i.e. VirtualBox, QEMU, VMWare, etc.) with Debian. I used Bulleyes version for this project on my home server rather than using a VM, but either will work.
Install Docker for Debian on the VM
https://docs.docker.com/engine/install/debian/
Install the Docker Compse Plugin on the VM
https://docs.docker.com/compose/install/linux/

## 2. Docker Compose Setup
Clone the GitHub repository to the server under the desired user's home directory
Unpack all files under 'Docker' to the desired location
Run the command 'docker compose up -d' to start all the containers. This will setup the MQTT Broker, InfluxDB, and Grafana.

## 3. Delay Tolerant Gateway Setup
Install screen with the 'sudo apt-get install screen' command
Install Python if needed
Unpack the 'dtngw' folder into the desired dirctory
Create a new screen, 'screen -S dtngw'
Create a virtual environment, 'python -m venv [venv name]'
Input 'source c[venv name]/activate' to activate the virtual environment
Install necessary libraries, 'pip install -r requirements.txt'
Start DTNGW, 'python dtngw.py'
Verify Connected exit code = 0 and data is outputting to the terminal
Exit Screen (CTRL + A + D)

## 4. ESP32 Setup
Select 'Create New Project' button in the PlatformIO Tab on VSCode
Select the 'New Project' option in the PIO Home Tab
In the board field input 'ESP32' and select your ESP32 board
Keep 'Arduino' as the default Framework
Select 'Finish'
Clone this GitHub repository, the ESP32/src directory contains the C++ files to copy over to your project
Create a 'wifi_secrets.h' header fil under the 'include' directory
Define two constants 'SECRET_SSID' with your WiFi SSID name and 'SECRET_PASS' with your WiFi password
In 'src/MQTT.cpp' edit the 'broker' variable to be the hostname ir IP address of the server
Wire the hardware using the schematic shown below
![Circuit Diagram](https://github.com/bkhutton/CSE696/blob/master/Circuit_Diagram.png?raw=true)
Plug the USB Micro-B to USB Type-A into your PC and ESP32
Select the PlatformIO tab and select 'Upload and Monitor'. This will upload the code to the ESP32 and receive serial input from the ESP32.
Verify the ESP32 shows a connected signature to WiFi in the serial monitor. Note it will fail connecting to the MQTT Broker because it will be setup in the next step.