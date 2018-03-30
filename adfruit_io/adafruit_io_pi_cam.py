#
# Simple program to watch an Adafruit IO feed (switch), 
# capture a picture using the Raspberry Pi camera, then send the thumbnail to 
# an Adafruit IO feed
# 
# This creates a very simple security cam, where pictures can be captured 
# from an Adafruit IO dashboard 
# 
import base64
import time
from   Adafruit_IO import Client
from   picamera import PiCamera
from   PIL import Image

# Set ADAFRUIT_IO_KEY to your Adafruit IO key
ADAFRUIT_IO_KEY = 'your key goes here'

# If your Feeds have different names, change them here
ADAFRUIT_IO_CAMERA_SWITCH_FEED = 'picam-pictureswitch'
ADAFRUIT_IO_CAMERA_IMAGE_FEED  = 'picam-image'

#
# Capture a picture
#
def capture_still(image_size, vflip, file):
   camera = PiCamera()

   if image_size == 1:
      camera.resolution = (320,240)
   elif image_size == 2:
      camera.resolution = (640,480)
   else:
      camera.resolution = (1024,768)

   if vflip == True:
      camera.vflip = True
      camera.hflip = True

   try:
      camera.capture(file)
      camera.close()
      return True
   except:
      camera.close()
      return False


# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

#
# This loop will wait for the camera capture switch on Adafruit IO 
# This uses the REST client, rather than MQTT
# 
while True:
   time.sleep(5)
   data = aio.receive(ADAFRUIT_IO_CAMERA_SWITCH_FEED)
   print 'data recieved = ', data
   if data.value == 'WAIT':
      print('Capture picture!')
      time.sleep(2)
      capture_still(1, False, 'temp.jpg')
      thumb_fd = open('temp.jpg', 'r')
      img = Image.open(thumb_fd)
      thumb_size = 320, 240
      img.thumbnail(thumb_size)
      img.save('temp-thumb.jpg', img.format)
      thumb_fd.close()

      with open('temp-thumb.jpg', "rb") as imageFile:
         str = base64.b64encode(imageFile.read())
      print('encoded image as base64')
      aio.send(ADAFRUIT_IO_CAMERA_IMAGE_FEED, str)
      aio.send(ADAFRUIT_IO_CAMERA_SWITCH_FEED, 'SNAP') 
