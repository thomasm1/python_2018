# -*- coding: utf-8 -*-
 
# MaestasP6
# Programmer:Thomas Maestas
# Email: thomas76milton@gmail.com
# Purpose:  
'''
Move the functions in TuplesDistance into a library.
# 4. To create your library create a new python program.
# 5. Cut the functions from program 5 and paste them into your new library.
# 6.  functions in your library should include:
#   a. A function that displays a header.
#    b. A function that asks the user for a 2 points in space and returns the point
#    as either a tuple or a list lat and lon.
##    c. A function that calculates the distance between two points.

7. Finally remove the functions from program 5 and replace them with an import
statement for your new library. Replace the function calls in program 5 with
calls to the functions in your library (myLibrary.getPoint() vs just getPoint()
for example).
    ## 
To create your library create a new python program and define functions in that program.
4. This assignment is to create 2 libraries/modules. First one is required if you are
doing this version of the assignment. Second is optional.
    a. A library that contains functions to convert units from metric to imperial and
        vice -versa. You can use:
        i. Kilometers to miles
        ii. Yards to meters
        iii. Inches to centimeters
        iv. Fahrenheit to Celsius
        v. Pounds to kilogram
    Hint: Use keyword arguments to run the conversion based on the unit provided.
    b. A library that contains two functions.
        i. One function will take a string and convert to a list and then add a number to each item on the list. The output would look something like this: [(0,y), (1,d), (2,u)]
        ii. A second function will take a list of lists and sort them according to a specified field (the default is the first element). Hint: Use the sort function with the key parameter.
Test Case:
Create a while loop to ask for user input and call the functions in the metric conversion module.
'''
import MaestasP6_myLibrary
MaestasP6_myLibrary.header()
MaestasP6_myLibrary.get_location()  

import MaestasP6_converter
MaestasP6_converter.convert()


