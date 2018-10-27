
'''

Explorer pHAT
5V inputs and outputs, analog inputs and an H-Bridge motor driver make up the Explorer pHAT; a jack of all trades prototyping side-kick for your Raspberry Pi. Perfect for RPi Zero but works with A+/B+/2 too!
To get the pHAT set up and ready to go you can use the one-line product installer:
$curl -sS https://get.pimoroni.com/explorerhat | bash

import explorerhat
from time import sleep
explorerhat.light.red.on()
explorerhat.light.red.off()
explorerhat.light.red.blink(0.5, 0.2)
explorerhat.light.red.on()
explorerhat.light.red.off()
print('this works')

explorerhat.motor.one.forward(85) #values 0 to 100 (full power)
sleep(2)
explorerhat.motor.one.stop()
'''
#
import explorerhat
from time import sleep


def forward (channel, event):
    explorerhat.motor.one.forward()
    sleep(2)
    explorerhat.motor.one.stop() 

explorerhat.touch.one.pressed(forward)

def backward (channel, event):
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.two.stop() 

explorerhat.touch.two.pressed(backward)
 




