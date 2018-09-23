from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
#sense.show_message("Picademy")
green = (0, 255, 0)
red = (255, 0, 0)

while True:
    x = randint(0,7)
    y = randint(0,7)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    sense.set_pixel(x,y,r,g,b)
    sleep(0.2)
'''    
while True:
    x = randint(0,7)
    y = randint(0,7)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    sense.set_pixel(x,y,r,g,b)
    sleep(0.2)
'''

'''
#kill switch code:
from sense_hat import SenseHat
from random import randint
from time import sleep

color = (116, 20, 10)
x = 7
y = 1
sense.set_pixel(x, y, color)
'''
