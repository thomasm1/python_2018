
'''works
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
 




