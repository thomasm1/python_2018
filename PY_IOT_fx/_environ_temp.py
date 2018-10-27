from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
 
blue = (0,0,255)
yellow = (255,255,0)
red = (255, 0, 0) 
sense_data = ('Tech Tuesday Temp Dashboard' ) 
sense.show_message(sense_data, text_colour=yellow, back_colour=blue, scroll_speed=0.075)
  
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
        sense.clear(blue) # BLUE  0,0,255
    elif t > 73: 
        sense.clear(255,0,0) # RED
    else:
        sense.clear(0,255,0) # GREEN
    sleep(0.8)
    
     
