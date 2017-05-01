# DHT Python library

This simple class can be used for reading temperature and humidity values from DHT11/DHT22/AM2302 sensors on Raspberry Pi.

# Usage

1. Instantiate the `DHT` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHTResult` object with actual values and error code.

For example:

```python
import RPi.GPIO as GPIO
import dht

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht.DHT(pin = 14)
result = instance.read()

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `dht_example.py` (you probably need to adjust pin for your configuration)


# License

This project is licensed under the terms of the MIT license.
