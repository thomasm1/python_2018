# -*- coding: utf-8 -*-
#MaestasP1
#Programmer: Thomas Maestas
#EMail: tmaestas29@cnm.edu
#Purpose: Area of Triangle Calculator

"""
Created on Wed Sep 17 18:44:38 2017

@author: tom
"""
print("Welcome to your personalized triangle calculator!")
print('')
height = float(raw_input('What is the height of the triangle? '))
base = float(raw_input('What is the base of the triangle? '))
area = float((base*height)/2)
#
print("Your entry for the height of triangle:  ", str(base))
print("Your entry for base length of triangle:  ", str(height))
print("Congratulations! Your Personalized Triangle Area Query is Ready!")
print("The calculated area of triangle is:  ",  area) 
