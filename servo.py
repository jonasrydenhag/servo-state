#!/usr/bin/python

import pymongo
import RPi.GPIO as GPIO
import time
import datetime
import sys
from pymongo import MongoClient
import singleLed

pinNr = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinNr, GPIO.OUT)

p = GPIO.PWM(pinNr,50)
p.start(7.5)
time.sleep(0.25)
p.ChangeDutyCycle(6.4)
time.sleep(0.2)
p.ChangeDutyCycle(7.5)
time.sleep(0.25)
p.stop()

GPIO.cleanup()

client = MongoClient('localhost', 27017)
db = client['temperature-station']
switches = db.switches

newSwitch = {
 	"date": datetime.datetime.utcnow()
}

for switch in switches.find().limit(1).sort("date", -1):
	if switch['state'] == 'on':
		newSwitch['state'] = 'off'
	elif switch['state'] == 'off':
		newSwitch['state'] = 'on'
	else:
		sys.exit()

switches.insert_one(newSwitch)

if newSwitch['state'] == 'on':
	singleLed.run()
