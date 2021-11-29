import sys
import time
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x0403, idProduct=0x6010)
if dev is None:
    dev = usb.core.find(idVendor=0x0403, idProduct=0x6001) # FT232BM

if dev is None:
    dev = usb.core.find(idVendor=0x4348, idProduct=0x55e0) # WCH bootloader
    if dev is None:
        print("No devices are found.")
        sys.exit()
else:    
    try:
        dev.ctrl_transfer(0x40, 0x91, 0, 0, 0)
    except usb.core.USBError as e:
        print('Apply magic success.')

retryCounter = 20
while retryCounter:
    print(".", end="")
    retryCounter = retryCounter - 1
    dev = usb.core.find(idVendor=0x4348, idProduct=0x55e0)
    time.sleep(0.5)
    if dev is not None:
        break
print("CH552 is now in DFU mode.")