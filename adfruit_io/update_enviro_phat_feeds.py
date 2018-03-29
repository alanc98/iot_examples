#
# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony DiCola
#
# Modified to send data from the Pimoroni EnviroPhat by Alan Cudmore
#

# Import Adafruit IO REST client.
import time
from   Adafruit_IO import Client
from   envirophat import light, weather, motion, analog

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'your key goes here'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

while True:
   temp = weather.temperature()   
   pressure = weather.pressure()
   lux = light.light()
   print 'Temperature is: ', temp
   print 'Pressure is: ', pressure 
   print 'Lux is: ',lux
   #
   # Your Adafruit IO feeds will probably have different names
   # Whatever you name them..  
   #
   aio.send('raspberrypi1-envirophat-temperature', temp)
   aio.send('raspberrypi1-envirophat-pressure', pressure)
   aio.send('raspberrypi1-envirophat-lux', lux)

   # Send these values to Adafruit IO 
   # every 10 seconds
   time.sleep(10)

