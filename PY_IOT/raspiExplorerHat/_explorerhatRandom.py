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

