
#!/usr/bin/env python

import os
from threading import Timer
from time import sleep
import RPi.GPIO as GPIO
import datetime         #debug


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

1waspressed = 0
2waspressed = 0
3waspressed = 0

# Timer Setup

def debugtimer():
        timestamp = []
        today = datetime.datetime.time(datetime.datetime.now())
        timestamp.append(today)
        print str(timestamp[0])
        debug = Timer(30.0, debugtimer)
        debug.start()

def background1():
        os.system('aplay longbell.wav &')
        global b1
        b1 = Timer(30.0, background1)
        b1.start()
        
def background2():
        os.system('aplay longbell.wav &')
        global b2
        b2 = Timer(30.0, background2)
        b2.start()
        
def background3():
        os.system('aplay longbell.wav &')
        global b3
        b3 = Timer(30.0, background3)
        b3.start()

def backgroundlong1():
        b1 = Timer(90.0, background1)
        p1 = Timer(90.0, pressreset1)
        b1.start()
        p1.start()
        global 1waspressed
        1waspressed = 1
        
def backgroundlong2():
        b2 = Timer(90.0, background2)
        p2 = Timer(90.0, pressreset2)
        b2.start()
        p2.start()
        global 2waspressed
        2waspressed = 1
        
def backgroundlong3():
        b3 = Timer(90.0, background3)
        p3 = Timer(90.0, pressreset3)
        b3.start()
        p3.start()
        global 3waspressed
        3waspressed = 1

def pressreset1():
        global 1waspressed
        1waspressed = 0
        
def pressreset2():
        global 2waspressed
        2waspressed = 0
        
def pressreset3():
        global 3waspressed
        3waspressed = 0

def startupdelay():
        os.system('amixer sset Master 100% &')
        background1()
        background2()
        background3()
        debugtimer()

global b1
global b2
global b3
b1 = Timer(30.0, background1)
b2 = Timer(30.0, background2)
b3 = Timer(30.0, background3)
d = Timer(30.0, startupdelay)


# MAIN BODY

d.start()

while True:
        if (GPIO.input(23) == False and 1waspressed == 0):
                os.system('aplay HeartThrob.wav &')
                os.system('aplay gloria.wav &')
                b1.cancel()
                backgroundlong1()

        if (GPIO.input(24) == False and 2waspressed == 0):
                os.system('aplay HeartThrob.wav &')
                os.system('aplay gloria.wav &')
                b2.cancel()
                backgroundlong2()
                
        if (GPIO.input(25) == False and 3waspressed == 0):
                os.system('aplay HeartThrob.wav &')
                os.system('aplay gloria.wav &')
                b3.cancel()
                backgroundlong3()               

        sleep(0.8)


