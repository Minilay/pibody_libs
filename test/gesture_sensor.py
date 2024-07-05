from machine import Pin, I2C
from time import sleep
import PAJ7620

# Initialize I2C communication
i2c = I2C(id=1, scl=Pin(3), sda=Pin(2))

gest = PAJ7620.Gesture(i2c)
while True:
    print(gest.return_gesture())

    sleep(0.1)