#!/usr/bin/env python

import max7219.led as led
import time
import random

display = led.sevensegment(cascaded=1)

orgValue = float(13.90)
orgDecValue = orgValue/10
print orgDecValue
orgStringValue = str(orgDecValue)
printStringValue = orgStringValue[::-1]
printValue = float(printStringValue) 

try:
	while True:
		#display.write_number(deviceId=0, value=21, decimalPlaces=2)
		#display.write_number(deviceId=0, value=21, decimalPlaces=2, leftJustify=True)
		display.write_number(0, printValue, 10, 2, True, False);
		#works display.write_number(0, 175.2, 10, 2, True, False);
		#display.write_number(deviceId, value, base=10, decimalPlaces=0, zeroPad=False, leftJustify=False):
except KeyboardInterrupt:
	display.clear()

#time.sleep(2)
#display.clear()
#time.sleep(1)

#a = random.randint(-999, 9999)
#b = random.randint(-3223, 9999)

#try:
#	for x in range(500):
#	    a += random.random() * 10
#	    b -= 1
#	    c = a + b / random.random()
#	    print(a)
#	    display.write_number(deviceId=0, value=a, decimalPlaces=3)
#	    time.sleep(2)
#except KeyboardInterrupt:
#	display.clear()
