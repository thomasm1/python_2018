from math import pi

def triangle_area(base, height):
    try:
        area = .5*base*height
        print(area)
        return area
    except TypeError:
        print('enter a numeric value puh-lease')
triangle_area(1,1)

def circle_area(pi,radius):
    try:
        area = (pi * radius*radius)
        print(area)
        return area
    except TypeError:
        print('enter a numeric value puh-lease')
circle_area(1,1)

def trapezoid_area(base1, base2, height):
    try:
        area = (((base1 + base2)/2)*height)
        print(area)
        return area
    except TypeError:
        print('enter a numeric value puh-lease')
trapezoid_area(1,1,1)

print('# Answers are: ')
trapezoid_area(1,0,1)

 

                  
