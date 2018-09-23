from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

my_data = ('Here','is','my','data')
red = (255,0,0)
edinburgh = (55.9533, 3.1883)
smarties = ('red', 'orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown')
print(smarties)
print(smarties[0])

for color in smarties:
    print(color)

r = (255, 0, 0)
'''           
pet1 = [e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,s,
    e,g,g,g,y,w,y,e,
    e,g,g,g,g,y,y,s,
    e,g,e,g,e,g,e,e,
    e,e,e,e,e,e,e,e
    ]
pet2 = [e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,s,
    e,g,g,g,y,w,y,e,
    e,g,g,g,g,y,y,s,
    e,g,e,g,e,g,e,e,
    e,e,e,e,e,e,e,e
    ]
sense.set_pixels(pet1)
sense.set_pixels(pet2)
sense.clear()
'''
for i in range(33):
    sleep(0.5)
    sleep(0.5)
while True:
    acc = sense.get_accelerometer_raw()
        if acc['x'] > 2
            print('done')

'''
#Traffic Lights
from sense_hat import SenseHat
from time import sleep
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
w = (255, 255, 255)
e = (0, 0, 0)
p1 = [
    e, e, e, e, e, e, e, e,
    b, e, e, e, e, e, e, e,
    e, b, e, e, b, e, b, e,
    e, b, r, r, b, w, w, e,
    e, r, r, r, w, g, w, w,
    e, r, r, r, e, r, e, e,
    e, e, e, e, e, e, e, e
    ]
p2 = [
    e, e, e, e, e, e, e, e,
    b, e, e, e, e, e, e, e,
    e, b, e, e, b, e, b, e,
    e, b, r, r, b, w, w, e,
    e, r, r, r, w, g, w, w,
    e, r, r, r, r, w, w, e,
    e, e, r, e, r, e, e, e,
    e, e, e, e, e, e, e, e
    ]
def walking():
    for i in range(10):
        sense.set_pixels(p1)
        sleep(0.5)
        sense.set_pixels(p2)
        sleep(0.5)
'''
