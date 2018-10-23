# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas

'''
ERROR MESSAGE 
 RESTART: /home/pi/_PythonJupyter/IoTpython_Programs/chinook/chinookSafety.py 
Traceback (most recent call last):
  File "/home/pi/_PythonJupyter/IoTpython_Programs/chinook/chinookSafety.py", line 47, in <module>
    safety(pitch, roll, yaw)
  File "/home/pi/_PythonJupyter/IoTpython_Programs/chinook/chinookSafety.py", line 37, in safety
    if p < 300:
TypeError:
'''

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
blue = (0,0,255)
yellow = (255,255,0)
red = (255, 0, 0) 
my_data = ('This Chinook dedicated to IOT-1296...' )
sense.show_message(my_data, text_colour=yellow, back_colour=red, scroll_speed=0.1)

def pitch():
    data = sense.get_orientation()
    pitch = data['pitch']
    print('Chinook pitch: ')
    print(pitch)
    return pitch

def roll():
    data = sense.get_orientation()
    roll = data['roll']
    print('Chinook roll: ')
    print(roll)
    return roll

def yaw():
    data = sense.get_orientation()
    yaw = data['yaw']
    print('Chinook yaw: ')
    print(yaw)
    return yaw 

def safety(): 
    sense = SenseHat()
    blue = (0,0,255)
    yellow = (255,255,0)
    red = (255, 0, 0) 
    my_data = ('This Chinook dedicated to IOT-1296...' )
    while pitch < 300.0:
        my_data = ('Warning!! pitch < 300')
    while roll < 300.0:
        my_data =('Warning!! roll < 300')
    while yaw < 300.0:
        my_data = ('Warning!! yaw < 300')
    my_data = ('This Chinook dedicated to IOT-1296...' )
    sense.show_message(my_data, text_colour=yellow, back_colour=red, scroll_speed=0.1)

pitch()
roll()
yaw()
# safety()


