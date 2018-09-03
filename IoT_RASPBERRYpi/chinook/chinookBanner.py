# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas
 

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
blue = (0,0,255)
yellow = (255,255,0)
red = (255, 0, 0) 
my_data = ('This Chinook dedicated to IOT-1296...' )
sense.show_message(my_data, text_colour=yellow, back_colour=red, scroll_speed=0.1)

 
