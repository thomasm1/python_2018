from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
t=sense.get_temperature()

print("TEMP, celsius :")
print(t)

f = t*9/5+32
print("TEMP, farenheit :")
print(f)
sense.show_message("Temperature Report")
sense.show_message("Red  > 80 ")
sense.show_message("Blue  < 70")

print("Red indicates > 75")
print("Green indicates < 75 && > 65")
print("Blue indicates < 65")
while True:
    t = sense.get_temperature()
    t = t*9/5+32
    print(t)
    if t < 65:
        sense.clear(0,0,255)
    if t > 80:
        sense.clear(255,0,0)

    else:
        sense.clear(0,255,0)
        
    sleep(0.5)

