# Environment Dashboard
# Tech Tuesday 9-26-18
# Thomas Maestas
# Abdul Gauba
 

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
'''
#
import explorerhat
from time import sleep
#
# press one - forward
'''
def forward (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor
    
def backward (channel, event):
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor
'''
def rotors (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor
'''
def lturn (channel, event):
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.forward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor
'''
explorerhat.touch.one.pressed(rotors)
#
 
'''
explorerhat.touch.two.pressed(backward)
explorerhat.touch.three.pressed(lturn)    
explorerhat.touch.four.pressed(rturn)
## press one - backward
def backward (channel, event):
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.two.stop() 
explorerhat.touch.two.pressed(backward)
##
def backward (channel, event):
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.two.stop() 
explorerhat.touch.two.pressed(backward)
'''
