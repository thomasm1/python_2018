#
# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas
'''works

import explorerhat
from time import sleep
explorerhat.light.red.on()
explorerhat.light.red.off()
explorerhat.light.red.blin
k(0.5, 0.2)
explorerhat.light.red.on()
explorerhat.light.red.off()
print('this works')
explorerhat.motor.one.forward(85) #values 0 to 100 (full power)
sleep(2)
explorerhat.motor.one.stop()
$curl -sS https://get.pimoroni.com/explorerhat | bash
'''
#
import explorerhat
from time import sleep

import _chinookBanner
_chinookBanner.banner()

import _chinookRotors
_chinookRotors.rotors()

# if switch -turned on... 
 ### then....
import _explorerMotorTurning
_explorerMotorTurning.forward()
_explorerMotorTurning.backward()
_explorerMotorTurning.lturn()
_explorerMotorTurning.rturn()
# else
### 
