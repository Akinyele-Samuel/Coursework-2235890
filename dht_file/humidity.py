#Complete Project Details: Humidity Readings.
#CM2110 Internet of Things
#Author -  Student number 2235890

#Based on Adafruit_CircuitPython_DHT

#Libraries
import sys
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

from time import sleep


while True:
        #Read Humidity from DHT22
        humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None:
            print("Humidity: {0.1f}%".format(humidity))
        
        else:
            print("Sensor failure, Please check wiring.")
        sleep(3) #Wait 3 seconds and read again 

