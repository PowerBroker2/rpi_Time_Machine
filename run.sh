#!/bin/bash

python gpsd_init_time_set.py
sudo pps-client &
pps-client -v