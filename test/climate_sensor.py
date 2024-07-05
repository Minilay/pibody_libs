
from machine import Pin, I2C
from time import sleep
import BME280

# Initialize I2C communication
i2c = I2C(id=1, scl=Pin(3), sda=Pin(2))

while True:
    try:
        # Initialize BME280 sensor
        bme = BME280.BME280(i2c=i2c)
        
        # Read sensor data
        tempC = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        
        # Convert temperature to fahrenheit
        
        # Print sensor readings
        print('Temperature: ', tempC)
        print('Humidity: ', hum)
        print('Pressure: ', pres)
        print()
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)

    sleep(0.05)