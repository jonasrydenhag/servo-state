#!/bin/bash

import RPi.GPIO as GPIO
import time

pinNr = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinNr, GPIO.OUT)

p = GPIO.PWM(pinNr,50)
p.start(7.5)
time.sleep(0.25)
p.ChangeDutyCycle(6.9)
time.sleep(0.2)
p.ChangeDutyCycle(7.5)
time.sleep(0.25)
p.stop()

GPIO.cleanup()
