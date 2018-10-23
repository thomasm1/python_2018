# Banner
# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas
# Running Lights
def lights()
    from gpiozero import LED
    led = LED(17)

    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

    # flashing --Testing Signal
    from gpiozero import LED
    led = LED(17)
    led.blink()
    led.blink(0, 0.5)

    # LED methods from https://gpiozero.readthedocs.io
    led.on()
    led.blink()
    led.toggle()
    led.pin.number # return pin number
    print(led.is_lit) # returns state

    # Traffic

    from gpiozero import LED
    from time import sleep
    red = LED(21)
    amber = LED(20)
    red = LED(16)

    red.on()
    sleep(3)
    red.off()
    amber.on() 

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

