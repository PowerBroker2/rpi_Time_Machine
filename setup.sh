#!/bin/bash

# Setup GPSD (used for setting initial time)
sudo apt-get update
sudo apt-get install gpsd-clients
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket

#########################################################
#########################################################
#### NOTE: MUST ALSO FOLLOW EXTRA INSTALL INSTRUCTIONS
#### FOUND HERE: https://github.com/rascol/PPS-Client
#########################################################
#########################################################

