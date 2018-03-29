#!/usr/bin/python
#
# This example tries to calibrate the sense hat temperature data by
# reading the Raspberry Pi CPU temperature averaging the two 
#
from sense_hat import SenseHat
import os

sense = SenseHat()
temp = sense.get_temperature()
t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
cputemp = t.read()
cputemp = cputemp.replace('temp=','')
cputemp = cputemp.replace('\'C\n','')
cputemp = float(cputemp)
print(" Sense Temp = ", temp)
print(" CPU Temp = ",cputemp)
newtemp = temp - ((cputemp - temp) / 2)
print("%.1f C" % newtemp)

