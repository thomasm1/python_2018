'''
Explorer pHAT
5V inputs and outputs, analog inputs and an H-Bridge motor driver make up the Explorer pHAT; a jack of all trades prototyping side-kick for your Raspberry Pi. Perfect for RPi Zero but works with A+/B+/2 too!
To get the pHAT set up and ready to go you can use the one-line product installer:
$curl -sS https://get.pimoroni.com/explorerhat | bash
'''
import explorerhat
from time import sleep
from random import randint

def wheel (channel, event):
    duration = randint(1,10)
    print(duration)
    explorerhat.motor.one.forward(100)
    sleep(duration)
    explorerhat.motor.one.stop()

explorerhat.touch.one.pressed(wheel)

