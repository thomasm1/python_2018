# Banner
# Project Chinook
##Authors
# Lewis Pilaroscia
# Thomas Maestas
# blinking
def banner()
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

