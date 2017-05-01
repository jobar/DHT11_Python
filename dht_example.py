import RPi.GPIO as GPIO
import dht
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht.DHT(pin=4)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %f C" % result.temperature)
        print("Humidity: %f %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)
    time.sleep(3)
