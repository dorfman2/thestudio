#!/usr/bin/env python

import os 
from time import sleep 

import RPi.GPIO as GPIO 


GPIO.setmode(GPIO.BCM) 
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

while True:
	if (GPIO.input(23) == False):
		os.system('aplay  kerrmoorpraise.wav &')

	if (GPIO.input(24) == False):
		os.system('aplay gloria.wav &')

	sleep(0.3);
