# vplate-server-pi3
server side on pi3 for vplate
inspired by this repo: [raspberry-server](https://github.com/darlinglele/raspberry-server) (However the code in this repo is somewhat buggy with python3 on pi3 and the socket connection with android)
### client side running on android
The client side code is in this repo: [vplate-client-andriod](https://github.com/RSLi/vplate-client-android)
## Requried hardwares
+ Raspberry pi3 * 1
+ H bridge * 1
+ motors * 1
+ jumpers
### Schematics produced with KiCAD can be found in the folder schematics 
  - or a pdf version: [schematic](Schematic/vplate.pdf)
## Usage
+ Connect the jumpers and wires with motor and pins
+ Setup the static IP on the Wireless Module on Raspberry pi3
+ Replace the HOST in car.py with your own IP address
+ run the server with sudo mode
## Idea
Server build up a socket connection with the andriod app. 
Server on the Raspberry pi3 will listen the data from the andriod app and convert the data to GPIO ouput to drive the motors

