from math import pi 
import _area

radius = 15
base = 4
base1 = 1
base2 = 2
radius = 15
height = 10
def request():
        for i in raw_input('list triangle-base+height, circle-radius or trapezoid-base1+base2+height'):
             print(i)
        print(_area.triangle_area(base,height))
        print(_area.circle_area(pi,radius))
        print(_area.trapezoid_area(base1,base2,height))
request()
