#!/usr/bin/env python

#author: Mouaiad Salaas
#date:   14.12.2020

#this simple code to read uart using usb

#importing time and serial libs 
import time
import serial

#defining our serial:
#from :                usb
#speed:                9600
#stop bits:            one
#size of transmision:  eight bits
ser = serial.Serial(
        port='/dev/ttyUSB0', 
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

#starting reading
while 1:
        x=ser.readline()
        print x,
