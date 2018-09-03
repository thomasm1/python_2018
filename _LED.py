# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:48:39 2017

@author: tom
"""
# Flashing LED
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

led.blink(5)
led.blink(2,0,0.5)
led.blink(0.1,10)
led.blink(0.5,0.5,5, False)

led.blink()
led.toggle()
led.pin.number
led.is_lit
