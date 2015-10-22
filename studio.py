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

waspressed1 = 0
waspressed2 = 0
waspressed3 = 0

t1 = 150.0
t2 = 71.0
t3 = 120.0
t4 = 66.0
t5 = 240.0
t6 = 68.0

# Timer Setup

def debugtimer():
        timestamp = []
        today = datetime.datetime.time(datetime.datetime.now())
        timestamp.append(today)
        print str(timestamp[0])
        debug = Timer(30.0, debugtimer)
        debug.start()

def background1():
        os.system('aplay bird_nat_2.wav &')
        global b1
        b1 = Timer(t1, background1)
        b1.start()
        
def background2():
        os.system('aplay cat_nat_3.wav &')
        global b2
        b2 = Timer(t3, background2)
        b2.start()
        
def background3():
        os.system('aplay cafe_nat_3.wav &')
        global b3
        b3 = Timer(t5, background3)
        b3.start()

def backgroundlong1():
        bl1 = Timer(t2, background1)
        p1 = Timer(t2, pressreset1)
        bl1.start()
        p1.start()
        global waspressed1
        waspressed1 = 1
        
def backgroundlong2():
        bl2 = Timer(t4, background2)
        p2 = Timer(t4, pressreset2)
        bl2.start()
        p2.start()
        global waspressed2
        waspressed2 = 1
        
def backgroundlong3():
        bl3 = Timer(t6, background3)
        p3 = Timer(t6, pressreset3)
        bl3.start()
        p3.start()
        global waspressed3
        waspressed3 = 1

def pressreset1():
        global waspressed1
        waspressed1 = 0
        
def pressreset2():
        global waspressed2
        waspressed2 = 0
        
def pressreset3():
        global waspressed3
        waspressed3 = 0

def startupdelay():
        os.system('sudo amixer sset Master 100% &')
        background1()
        background2()
        background3()
        debugtimer()

global b1
global b2
global b3

b1 = Timer(t1, background1)
b2 = Timer(t3, background2)
b3 = Timer(t5, background3)
d = Timer(1.0, startupdelay)


# MAIN BODY

d.start()

while True:
        if (GPIO.input(23) == False and waspressed1 == 0):
                os.system('aplay bird_mus_1.wav &')
                b1.cancel()
                backgroundlong1()

        if (GPIO.input(24) == False and waspressed2 == 0):
                os.system('aplay cat_mus_2.wav &')
                b2.cancel()
                backgroundlong2()
                
        if (GPIO.input(25) == False and waspressed3 == 0):
                os.system('aplay cafe_mus_1.wav &')
                b3.cancel()
                backgroundlong3()               

        sleep(0.8)
