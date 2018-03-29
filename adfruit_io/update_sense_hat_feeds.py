# 
# This is an example program of how to read data 
# from the Raspberry Pi Sense hat and send it to
# Adafruit IO 
#   
import time
from Adafruit_IO import Client
from sense_hat import SenseHat

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'put your key here'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

# Initialize the sense hat
sense = SenseHat()

while True :
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    calctemp = 0.0071*temp*temp+0.86*temp-10.0
    calchum=humidity*(2.5-0.029*temp)
    print 'pressure: %.0f, temp: %.1f, humidity: %.0f' % (pressure, calctemp, calchum)

    #
    # Send the temperature to an Adafruit IO feed
    # The name of your feed will probably be different
    #
    # You can also send other data values such as humidity and 
    # pressure to other feeds 
    #
    aio.send('raspberrypi1-sensehat-temperature', calctemp)
    aio.send('raspberrypi1-sensehat-pressure', pressure)
    aio.send('raspberrypi1-sensehat-humidity', humidity)

    time.sleep(10)
