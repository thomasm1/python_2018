# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:33:09 2017

@author: tom
"""
# MaestasP4
# __4inputGames
#DEF: not defined yet
# Programmer:Thomas Maestas
# Email: thomas76milton@gmail.com
''' Purpose: program that will ask the user if they would like to play a game, will open a web browser to that game, then
loop back to ask the user if they would like to do another.
a. Import web browser library (import webbrowser)
b. Create a variable called response and initialize it to ‘y’
c. Start a while loop that loops as long as response is ‘y’
d. Ask the user “Would you like to play a game? “ (use raw_input). Store the response in the response variable.
e. If the response is ‘yes’ display a menu using print command. Or, you can store the Games as a list and display the list using the for loop.
CHESS
TIC TAC TOE
TETRIS
COUNT
f. Use a raw_input command to get the users selection and store it into a variable (call it game for example)
g. Use if, elif and a final else command to check the users response an do the following:
i. If game has the word ‘chess’ then open a webrowser using the following command: webbrowser.open_new(“http://www.pygame.org/tags/chess")
ii. Else If game has the word ‘tic tac toe’ then open a webrowser using: webbrowser.open_new("http://www.pygame.org/tags/tictactoe")
iii. Else if game has the word ‘tetris’ then open a webrowser using: webbrowser.open_new("http://www.pygame.org/tags/tetris")
iv. Else if game has the word ‘count’ then:
1. Ask the user ‘how high’ and store that in a variable (say maxNumber)
2. Use a for loop to print each number in the range from zero to that number (use range(maxNumber)).
v. Else if it doesn’t meet any of the conditions above just print “I did not understand that!”
TestCases:
1. Run the program once with a ‘y’ value and select one of the three games (Chess, Tictactoe, Tetris). Then in the second iteration, select count, provide a number.
Note: As long as the value is ‘y’ the loop will not terminate. You have to close the program and rerun it again.
2. Run the program with a value of ‘n’.
 '''
import webbrowser
import pprint

response = 'y'
while response == 'y':
    print('You\'re Welcome !')
    ask = raw_input('Would you like to play a game? (type menu at any time) \'y\' or \'n\' ...\n__.otM==>>')
    response = ask
    menu = ['chess', 'tic tac toe', 'tetris','count']
    if response == 'y':
        pprint.pprint(menu)
        whichGame = raw_input('Which then among those listed ? ')
        if whichGame == 'chess':
            webbrowser.open_new("http://www.pygame.org/tags/chess")
        elif whichGame == 'tic tac toe':
            webbrowser.open_new("http://www.pygame.org/tags/tictactoe")
        elif whichGame == 'tetris':
            webbrowser.open_new("http://www.pygame.org/tags/tetris")
        elif whichGame == 'count':
            jump = raw_input("how high must one count? \n ")
            maxNumber = int(jump)
            for i in range(maxNumber):
                pprint.pprint(i)
    elif response == 'n':
        print(' well, okay !')
    else:
        print(' Didn\nt understand. Well, please come again when you can decide ! ')
        
    
    
