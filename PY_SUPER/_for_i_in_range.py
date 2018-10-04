# -*- coding: utf-8 -*-
"""
!! PYTHON 3.X ONLY !!
Created on Tue Sep 19 22:44:52 2017
@author: tom
"""
print("Python-Python")
print('########## RANGE(x)')
for i in range(4):
    print(i)
    
print('############ FOR')
stuff = ['a','b','c']     ##  gives access to element
quantity = [4,6,9]
for i in stuff:
    print(i) 

print('########## RANGE(LEN())')
for i in range(len(stuff)):  ## gives index
    print(i)
    
print('########## ENUMERATE(i,j)')
for i, j in enumerate(stuff, start = 1):
    print(i, j)

print('######## ZIP(i,j)')
for i, j in zip(stuff,quantity):
    print(i, j)
 
print('######## list in list # print(x[1][3] ') 
nested = [['a','b','c','d'],[1,2,3,4]]
print(nested[1][2])

print('######## quantity[stuff[0].index(\'a\')')
nested_index = nested[0].index('c')
print(nested_index)

print('######## quantity[stuff.index(input)')
a = input("enter a thing, a thru c ")       
stuff_index = quantity[stuff.index(a)]
print(stuff_index)

