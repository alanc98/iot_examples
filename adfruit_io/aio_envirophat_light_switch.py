#
# Example of how to control the LED lights on an EnviroPhat 
#  from an Adafruit IO switch
#
#  The Adafruit IO switch is a data feed that is displayed as a button
#  on a Dashboard. 
#  When the user flips the switch, this program will notice the change
#  the next time it reads the feed. When the feed value changes 
#  from OFF to ON, it turns on the LED lights. 
#
#  Adafruit IO also allows you to use MQTT to notify your program when
#  a change is made, but the connection does time out if it sits
#  for a while. This is why the switch is polled using the REST API.
# 
# 
import sys
import time
from   envirophat  import leds
from   Adafruit_IO import Client

# Put your Adafruit IO key here:
ADAFRUIT_IO_KEY      = 'key goes here'
aio = Client(ADAFRUIT_IO_KEY)

while True:
   time.sleep(5)
   # 
   # Read the switch feed. Your switch may be called something else
   # ( whatever you decide to name it )
   #
   data = aio.receive('raspberrypi1-envirophat-ledswitch')
   print 'data recieved = ', data
   if data.value == 'ON':
      leds.on()
   else:
      leds.off()


