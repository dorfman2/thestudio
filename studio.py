#!/usr/bin/env python

###By Jeff Dorfman for DC Artomatic 2015

import os
from threading import Timer
from time import sleep
import RPi.GPIO as GPIO
import datetime         #debug


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

waspressed = 0

# Timer Setup

def debugtimer():
        timestamp = []
        today = datetime.datetime.time(datetime.datetime.now())
        timestamp.append(today)
        print str(timestamp[0])
        debug = Timer(1800.0, debugtimer)
        debug.start()

def background():
        os.system('aplay longbell.wav &')
        global t
        t = Timer(30.0, background)
        t.start()

def backgroundlong():
        d = Timer(90.0, background)
        p = Timer(90.0, pressreset)
        d.start()
        p.start()
        global waspressed
        waspressed = 1

def pressreset():
        global waspressed
        waspressed = 0

def startupdelay():
        os.system('amixer sset Master 100% &')
        background()
        debugtimer()

a = Timer(30.0, startupdelay)


def startupdelay():
        os.system('amixer sset Master 100% &')
        background()
        debugtimer()

a = Timer(30.0, startupdelay)

# MAIN BODY

a.start()

while True:
        if (GPIO.input(23) == False):
                os.system('aplay kerrmoorpraise.wav &')

        if (GPIO.input(24) == False and waspressed == 0):
                os.system('aplay HeartThrob.wav &')
                os.system('aplay gloria.wav &')
                t.cancel()
                backgroundlong()

        sleep(1)
