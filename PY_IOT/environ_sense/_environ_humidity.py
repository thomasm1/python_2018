from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
h=sense.get_humidity()

print("Humidity :")
print(h)
  
print("Red indicates > 45")
print("Green indicates < 45 && > 10") 
while True:
    h = sense.get_humidity() 
    print(h) 
    if h > 40:
        sense.clear(255,0,0)

    else:
        sense.clear(0,255,0)
        
    sleep(0.5)  