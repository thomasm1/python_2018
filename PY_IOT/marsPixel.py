'''
Scroll_speed:  default value is 0.1. The bigger number lower the speed.
text_colour:    colour of the text  defined via three values to specify red, green, and blue. These are also called RGB values.
'''
from sense_hat import SenseHat
from time import sleep
'''
import webbrowser.sys 

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'http://www.thomasmaestas.net/marsreader.index.php'
print(my_url)
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
'''











 
sense = SenseHat() 
my_data = ('Mars temperature Nov 3' + '2017-11-09:Big, beautiful spiral galaxy NGC 1055 is a dominant member of a small galaxy group a mere 60 million light-years away toward the aquatically intimidating constellation Cetus.')
 
blue = (0,0,255)
yellow = (255,255,0)
red = (255, 0, 0) 
r = 255
g = 255
b = 255

sense.show_message(my_data, text_colour=yellow, back_colour=blue, scroll_speed=0.1)

for i in range(33):
    sleep(0.5)

sense.clear((r, g, b))
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
