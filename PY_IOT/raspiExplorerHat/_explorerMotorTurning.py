"""
Installing The Library: The Easy Way Section from the GitHub ExplorerHat README.
Complete the Getting Started Section from the GitHub ExplorerHat README.
Complete the Explorer Hat Workshop Worksheet.
At this point you should understand how to control a single motor and there is enough code examples in the exercises to add a second motor.
Complete the following Tasks:
1.  Connect 2 motors to the Explorer Hat
2.  Program 4 Buttons to drive the motors as follows;
     2a.  Button 1 - Both motors move forward.
     2b.  Button 2. - Both motors move backwards.
     2c.  Button 3 - Motor One moves forward, Motor 2 moves backward
     2d.  Button 4 - Motor One moves backward, Motor 2 moves forward.
Take a video of this final working exercise and submit the video and your code as completion of this assignment.
BONUS POINTS:  If you can with a classmate build a functioning cardboard robot with the knowledge gained from this activity.
"""

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
#
# press one - forward

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

def rturn (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor

def lturn (channel, event):
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.forward(100)
    sleep(2)
    explorerhat.motor.one.stop() #Tom's motor
    explorerhat.motor.two.stop() # Lewis motor

explorerhat.touch.one.pressed(forward)    
explorerhat.touch.two.pressed(backward)
explorerhat.touch.three.pressed(lturn)    
explorerhat.touch.four.pressed(rturn)
'''

## press one - backward
def backward (channel, event):
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.two.stop() 
explorerhat.touch.two.pressed(backward)
#
#
def backward (channel, event):
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.two.stop() 
explorerhat.touch.two.pressed(backward)
 




'''
