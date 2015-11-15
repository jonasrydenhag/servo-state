import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

activated = 0

try:
	while True:
		if (GPIO.input(11) == 1):
			if (activated == 0):
				activated = 1
				print("true")
				time.sleep(2)
		else:
			activated = 0
				
except KeyboardInterrupt:
	GPIO.cleanup()
