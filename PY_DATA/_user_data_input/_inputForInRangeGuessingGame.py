# -*- coding: utf-8 -*-
"""
Spyder Editor

#Author: Thomas Maestas
#CIS 1096-IoT
"""
# 0 # eggs append !!
eggs = [1, 2, 3]
del eggs[2]
print eggs
eggs.append(99)
eggs.append(98)
print eggs
print len(eggs)
eggs.append('henry')
eggs = tuple(eggs)  # Tuple Conversion
print type(eggs)
print eggs
print
def legos(someParameter):
    someParameter.append('Hi, Im appended')
spam = [1,2,3]
legos(spam)
print(spam)
print
import copy
spama = ['A', 'B', 'C', 'D']
cheese = copy.copy(spama)
cheese[1] = 123
print spama
print cheese
print

# 1 # randomized fortune:
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
print('[1 2 3 ] + [t, o, m]')
print [1,2,3] + ['t','o','m']
print

# 2 # Guessing Game
import random
secretNumber = random.randint(1, 11)
print('I am thinking of a number between 1 and 10.')
for guessesTaken in range(1,5):
    print('Take a guess.')     
    guess = int(input())
    if guess < secretNumber:
        print('your guess is too low.')
    elif guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    elif guess > secretNumber:
        print('your guess is too high.')
    else:
        print('Nope, try again')
        break # condition correct!
