from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
 
t = sense.get_temperature()
t = t-15.0 # calibrate
t = t* (9/5) + 32.0
sense.show_message("Temp:")
temp = t 
 
while True:
    t = sense.get_temperature()
    t = t-15.0 # calibrate
    t = t* (9/5) + 32.0
    print(t)
    if t < 70:
        sense.clear(0,0,255) # BLUE
    if t > 73: 
        sense.clear(255,0,0) # RED
    else:
        sense.clear(0,255,0) # GREEN
    sleep(0.8)
    
     
