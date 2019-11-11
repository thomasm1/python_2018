# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:33:09 2017
@author: tom
###Part I.
# 1.	Write a program that stores contact information and allows you to retrieve it.
# 2.	Your program will initialize a list of names and phone numbers.  Have atleast 4 names and phone numbers.
# 3.	Display the list of names to the user.
# 3.	Next ask the user to enter a name.
###Part II.
# 7.	Check if the name exists in the list (checking for membership)
# 8.	Find the index of that name and the corresponding phone number using the index.
# 9.	Report back to the user that person’s phone number.
"""
# MaestasP2
# Programmer:Thomas Maestas
# Email: tmaestas29@cnm.edu
# Purpose: Provides user capability to view contact info

###Part I. -Initialize core database population
thomas = ['Thomas Maestas', '505-508-7707']
sarah = ['Sara Treviso', '410-333-3399']
tom2 = ['Thomas Maestas', '505-463-7259']
s2 = ['Sara Two Treviso', '410-333-3366']

database = [thomas,sarah,tom2,s2]
print
print ('Current Database Population:')
print(database)
print
print('Plz add your name and number to the database...')
username = raw_input('Plz Parenthesize Your Contact Information. First & Last Name: ',)
phonenum = raw_input('Phone Number: ')
newUser = [username, phonenum]
database += newUser
print ('Updated Database Population:')
print(database)
print
print('There you go, your name and number are added!')
print

##Part II.
db = []
print ('Would you like to search a name, to save you time?')
print
inquiry = raw_input('name or number, even a fragment will do : ')
if inquiry in database[0]: print 'Yes, name and number in file'
else: print 'sorry, not found! Try again soon'
print
print(database)


# friendNames = []
# name = ''
# while True:
#     print('Register all your cat phone numbers, Entry #' + str(len(friendNames) + 1) + '.  After entering all numbers, hit ENTER. Use comma, like: xxx-xxx-xxxx, Tom ')
#     name = input()
#    if name == '':
 #        break
 #    friendNames = friendNames + [name] # list concat
 #    print('The names are:')
 #    for name in friendNames:
#         print(' ' + name)





