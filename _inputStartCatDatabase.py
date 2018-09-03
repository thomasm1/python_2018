# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#random
print('')
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return '(1) Your day will be mundane, so look for novelty in little things'
    elif answerNumber == 2:
        return '(2) Your day will be fast! Slow, and be sure to not make waste in the haste'
    elif answerNumber == 3:
        return '(3) Your day portends great things: capture your fate!'
print('Welcome to this Good Fortune Page, and your fate reads that : ')
print 
print(getAnswer(random.randint(1,4)))
print 
#List-making app
catNames = []
name = ''
while True:
    print('Register all your cat phone numbers, Entry #' + str(len(catNames) + 1) + '.  After entering all numbers, hit ENTER to stop. Use comma between number and name, like: xxx-xxx-xxxx, Tom ')
    name = raw_input()
    if name == '':
        break
    else:
        catNames = catNames + [name] # list concat
print('The cat names are:')
for name in catNames:
    print(' ' + name)
    
