# -*- coding: utf-8 -*- 
# MaestasP5
# Programmer:Thomas Maestas
# Email: tmaestas29@cnm.edu
''' Purpose: Program that calculates the distance between two geographic points.
4. Your program will have the following functions
	4.1. A “header” function that takes no parameters and returns nothing that displays a header. The header will print a summary explaining the purpose of the program.
	4.2. A “get_location” function that takes no parameters, asks the user for a latitude and longitude and returns a tuple or list with the latitude and longitude. Make sure you tell the user what units to enter their information in!
	4.3. A “distance” function that takes two tuples, each with a latitude and longitude, calculates the distance between those two geographic points and returns the distance. You will search online for a formula to use. Make sure you cite in comments the source of your formula and give credit to the source of this information (Name of person or organization and web link). Note, you may not use an existing library for this function. You must have the formula encoded in your function directly.
5. In the main part of the program (after declaring your functions):
	5.1. Call the Header function that displays a header.
	5.2. Program should allow the user to do multiple calculations. Use a “do another?” loop.
	5.3. Inside the loop the program will do the following:
	5.3.1.Call the get_location function to get the first location.
	5.3.2.Call the get_location function again to get the second location.
	5.3.3.Call the distance function passing in the two locations above as arguments.
	5.3.4.Display a nicely formatted message to the user telling them the distance between those two
	locations.
	5.3.5. Finally ask the user if they want to do another.
6. When done display a good bye message outside the loop.

**
URL SOURCE FOR DISTANCE FORMULA:
https://stackoverflow.com/questions/5228383/how-do-i-find-the-distance-between-two-points
**
Santa Fe Coordinates: y = 35.687, x= 105.938
Albuquerque Coordinates: y=35.085, x=106.606
'''
def header():  # Header Function 
    print("""
Welcome to the Great 
Python Header Featurette! 
             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/
      <3, __TMM__TMM__TMM__
""")
header()
print
import math
def get_location(): 
    xname = input('Enter location longitudinal coords: ')
    yname = input('Enter location latitudinal coords: ') 
    coords = []
    coords = [xname,yname]
    xx  = input('Enter 2nd location longitudinal coords: ')
    yy  = input('Enter 2nd location latitudinal coords: ')
    print(type(coords))
    #print(coords)
    def distance(x1,y1,x2,y2):  # I found this formula from stack_overflow - URL is cited in header.
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print('The distance between first site and second site is : ' + str(dist))
        #print(dist)
    distance(xx,yy,xname,yname)
    a = raw_input('any other coordinates? enter y or n... ' )
    def anotherQ(a):
        if a == 'y':
            print('yeah ?...')
            get_location()
        elif a == 'n':
            print('okay, goodbye!')
        else:
            print('well, can\'t decide? - goodbye anyway !! ')
    anotherQ(a)

get_location()
