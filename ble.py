#!/usr/bin/python

import btle
import struct
from btle import UUID

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        print "init"

    def handleNotification(self, cHandle, data):
        if data == "temp":
            svc = p.getServiceByUUID(UUID("bd011f22-7d3c-0db6-e441-55873d44ef40"))
            ch = svc.getCharacteristics(UUID("0503b819-c75b-ba9b-3641-6a7f338dd9bd"))[0]
            ch.write(struct.pack("B", 0x02))
            ch.write(struct.pack("B", 0x01))
            ch.write(struct.pack("B", 0x05))
            ch.write(struct.pack("B", 0x04))
            print "yeah baby!"

def _TI_UUID(val):
    return UUID("%08X-0451-4000-b000-000000000000" % (0xF0000000+val))

# Initialisation  -------

p = btle.Peripheral("20:76:86:0A:DB:D5")
p.setDelegate(MyDelegate())


# Setup to turn notifications on, e.g.


# Main loop --------

try:
    while True:
        if p.waitForNotifications(1.0):
            # handleNotification() was called
            print "recieved"
            continue

        print "Waiting..."
        # Perhaps do something else here

except KeyboardInterrupt:
    p.disconnect()

    print "Quit"

