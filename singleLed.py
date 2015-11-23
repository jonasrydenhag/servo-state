#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

PIR_PIN = 27

GPIO.setup(PIR_PIN, GPIO.OUT)

GPIO.output(PIR_PIN, True)
time.sleep(15)
GPIO.output(PIR_PIN, False)

GPIO.cleanup()
