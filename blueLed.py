#!/usr/bin/python
import sys
sys.path.insert(0, '/home/pi/bluepy/bluepy')

import temp
import btle
import struct
from btle import UUID

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        svc = p.getServiceByUUID(UUID("bd011f22-7d3c-0db6-e441-55873d44ef40"))
        self.ch = svc.getCharacteristics(UUID("0503b819-c75b-ba9b-3641-6a7f338dd9bd"))[0]

    def handleNotification(self, cHandle, data):
        if data == "temp":
            self.writeTemp()

    def writeTemp(self):
        for char in self.getTemp():
            self.ch.write(struct.pack("B", int(char)))

    def getTemp(self):
        h,t,date = temp.read()

        orgValue = round(t, 2)
        orgStringValue = str(orgValue)
        cleanStringValue = orgStringValue.replace('.', '')

        if len(cleanStringValue) < 4:
            cleanStringValue += "0"

        return list(cleanStringValue)


# Initialisation  -------
p = btle.Peripheral("20:76:86:0A:DB:D5")
p.setDelegate(MyDelegate())

# Main loop --------
try:
    while True:
        if p.waitForNotifications(1.0):
            # handleNotification() was called
            continue

except KeyboardInterrupt:
    print "Quit"

