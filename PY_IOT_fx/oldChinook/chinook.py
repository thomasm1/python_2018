# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas
'''works

explorerhat.motor.one.forward(85) #values 0 to 100 (full power)
sleep(2)
explorerhat.motor.one.stop()
$curl -sS https://get.pimoroni.com/explorerhat | bash
'''
#
import explorerhat
from time import sleep
from sense_hat import SenseHat

explorerhat.light.red.on()
explorerhat.light.red.off()
explorerhat.light.red.blink(0.5, 0.2)
explorerhat.light.red.on()
explorerhat.light.red.off()
print('Chinook Lights')

while True:
    acc = sense.get_accelerometer_raw()
    if acc['x'] > 2:
            print('done: acc x > 2')

import chinookSafety
chinookSafety.pitch()
chinookSafety.roll()
chinookSafety.yaw()
chinookSafety.safety()

import chinookRunning
chinookRunning.lights()

import chinookRotors
chinookRotors.rotors()

chinookRotors.forward()
chinookRotors.backward()
chinookRotors.lturn()
chinookRotors.rturn()
