from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    humidity = sense.get_humidity()

    if humidity > 29:
        sense.clear(255,0,0)
    else:
        sense.clear(0,0,255)

    sleep(0.1)
    
