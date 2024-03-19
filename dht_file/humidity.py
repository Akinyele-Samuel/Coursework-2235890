#Complete Project Details: Humidity Readings.
#CM2110 Internet of Things
#Author -  Student number 2235890

#Based on Adafruit_CircuitPython_DHT

#Libraries
from sense_hat import SenseHat

import sys
from time import sleep

# adapted from https://learn.adafruit.com/adafruit-io-basics-digital-output/python-code
#import Adafruit IO REST client.

from Adafruit_IO import Client, Feed, RequestError, Data
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = ''

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'Akinyele_Samuel'

sense = SenseHat()

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

TAG = "sensehat humidity publisher"




while True:
        #Read Humidity from DHT22
        humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        
        if humidity is not None:
            #To print the humidity and format it to one decimal place
            print("Humidity: {:.1f}%".format(humidity))
        
        else:
            print("Sensor failure, Please check wiring.")
        sleep(3) #Wait 3 seconds and read again 

