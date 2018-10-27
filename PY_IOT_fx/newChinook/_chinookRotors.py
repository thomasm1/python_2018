#
# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas

#
import explorerhat
from time import sleep
#
# press one - forward

def rotors (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor
 
explorerhat.touch.one.pressed(rotors)
 