#!/usr/bin/env python

import os
from threading import Timer
from time import sleep
import RPi.GPIO as GPIO
import datetime         #debug


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

waspressed1 = 0
waspressed2 = 0
waspressed3 = 0
waspressed4 = 0

t1 = 141.0
t2 = 70.0
t3 = 128.0
t4 = 70.0
t5 = 199.0
t6 = 90.0
t7 = 176.0
t8 = 85.0

# Timer Setup

def debugtimer():
        timestamp = []
        today = datetime.datetime.time(datetime.datetime.now())
        timestamp.append(today)
        print str(timestamp[0])
        debug = Timer(30.0, debugtimer)
        debug.start()

def background1():
        os.system('aplay bird_nat_4.wav &')
        global b1
        b1 = Timer(t1, background1)
        b1.start()
        
def background2():
        os.system('aplay cat_nat_4.wav &')
        global b2
        b2 = Timer(t3, background2)
        b2.start()
        
def background3():
        os.system('aplay cafe_nat_4.wav &')
        global b3
        b3 = Timer(t5, background3)
        b3.start()

def background4():
        os.system('aplay type_nat_1.wav &')
        global b4
        b4 = Timer(t7, background4)
        b4.start()
        
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
        
def backgroundlong4():
        bl4 = Timer(t8, background4)
        p4 = Timer(t8, pressreset4)
        bl4.start()
        p4.start()
        global waspressed4
        waspressed4 = 1
        
def pressreset1():
        global waspressed1
        waspressed1 = 0
        
def pressreset2():
        global waspressed2
        waspressed2 = 0
        
def pressreset3():
        global waspressed3
        waspressed3 = 0

def pressreset4():
        global waspressed4
        waspressed4 = 0
        
def startupdelay():
        os.system('amixer sset Master 100 &')
        background1()
        background2()
        background3()
        background4()
        debugtimer()

global b1
global b2
global b3
global b4

b1 = Timer(t1, background1)
b2 = Timer(t3, background2)
b3 = Timer(t5, background3)
b4 = Timer(t7, background4)
d = Timer(15.0, startupdelay)


# MAIN BODY

d.start()

while True:                     
        if (GPIO.input(18) == False and waspressed1 == 0):
                os.system('aplay bird_mus_4.wav &')
                b1.cancel()
                backgroundlong1()

        if (GPIO.input(23) == False and waspressed2 == 0):
                os.system('aplay cat_mus_4.wav &')
                b2.cancel()
                backgroundlong2()
                
        if (GPIO.input(24) == False and waspressed3 == 0):
                os.system('aplay cafe_mus_4.wav &')
                b3.cancel()
                backgroundlong3()  
                        
        if (GPIO.input(25) == False and waspressed4 == 0):
                os.system('aplay type_mus_1.wav &')
                b4.cancel()
                backgroundlong4()     

        sleep(0.2)
