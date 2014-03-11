#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def blink(pin):  
        """blinking function"""
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return


# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
# set up GPIO output channel
GPIO.setup(7, GPIO.OUT)
# blink GPIO17 50 times
for i in range(0,50):
        blink(7)
        
GPIO.cleanup()