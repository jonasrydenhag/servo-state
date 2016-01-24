#!/usr/bin/python

import bluetooth
import time

import pymongo
from pymongo import MongoClient
import datetime
import sys
import singleLed

bd_addr = "00:06:66:7A:D1:05"

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("push")

time.sleep(2)
sock.close()

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
