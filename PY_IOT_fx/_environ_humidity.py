from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
h=sense.get_humidity()

print("Humidity :")
print(h)

blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
red = (255, 0, 0) 
print("Red indicates > 40")
print("Green indicates < 40 && > 10") 
while True:
    h = sense.get_humidity() 
    print(h) 
    if h < 10:
        sense.clear(blue) #(0,0,255)
    if h > 40:
        sense.clear(red) #(255, 0, 0)
    else:
        sense.clear(green) #(0,255,0)        
    sleep(0.5)  