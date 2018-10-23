# Environment Dashboard
# Tech Tuesday 9-26-18
# Thomas Maestas
# Abdul Gauba
 

import explorerhat
from time import sleep
#
# press one - forward

def rotors (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop() # 1  motor
    explorerhat.motor.two.stop() # 2 motor
 
explorerhat.touch.one.pressed(rotors)
 
