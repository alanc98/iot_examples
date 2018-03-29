#
# Simple meteorology
# This was found on the raspberrypi.org forums as a code sample
# 
 
from sense_hat import SenseHat
import time

sense = SenseHat()

while True :
    #
    # Take readings
    # 
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    #
    # Try to calculate calibrated temperature
    #
    calctemp = 0.0071*temp*temp+0.86*temp-10.0
    calchum=humidity*(2.5-0.029*temp)
    print '%.0f %.1f %.0f' % (pressure, calctemp, calchum)
    time.sleep(5)
