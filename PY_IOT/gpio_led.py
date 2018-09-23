# blinking
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.blink()
    led.blink(0, 0.5, .5, 1, 1)
    led.blink(0, 0.5, .5, 1, 1)
    led.blink(0, 0.5, .5,0.5, 1, 1,0, 0.5, .5, ) 
    
# flashing
    led.on()
    sleep(1)
    led.off()
    sleep(1)
 
# LED methods from https://gpiozero.readthedocs.io

# led.on()

# led.blink()

# led.toggle()

# led.pin.number # return pin number

# led.is_lit # returns state

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

