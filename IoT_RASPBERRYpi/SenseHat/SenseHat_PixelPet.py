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