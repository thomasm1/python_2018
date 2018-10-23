# Environment Dashboard
# Tech Tuesday 9-26-18
# Thomas Maestas
# Abdul Gauba
 

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
blue = (0,0,255)
yellow = (255,255,0)
red = (255, 0, 0) 
sense_data = ('Tech Tuesday Temp Dashboard' ) 
sense.show_message(sense_data, text_colour=yellow, back_colour=blue, scroll_speed=0.075)
 
