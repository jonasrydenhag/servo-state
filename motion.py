#!/usr/bin/python

import RPi.GPIO as GPIO
import temp
import max7219.led as led

import time

GPIO.setmode(GPIO.BCM)

PIR_PIN = 4

GPIO.setup(PIR_PIN, GPIO.IN)

tempMeasuring = False

try:

	print "PIR Module Test (CTRL+C to exit)"

	time.sleep(2)

	print "Ready"

	while True:

		if GPIO.input(PIR_PIN) and not tempMeasuring:
			tempMeasuring = True

			h,t,date = temp.read()

			orgValue = round(t,2)
			orgDecValue = orgValue/10
			orgStringValue = str(orgDecValue)
			printStringValue = orgStringValue[::-1]
			printValue = float(printStringValue)

			display = led.sevensegment(cascaded=1)
			display.write_number(0, printValue, 10, 2, True, False);

			tempMeasuring = False
			time.sleep(4)
			display.clear()

		time.sleep(1)

except KeyboardInterrupt:

	print "Quit"

	GPIO.cleanup()
