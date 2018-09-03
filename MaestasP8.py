# MaestasP8
# Programmer: Thomas Maestas
# EMail: thomas76milton@gmail.com
# Purpose:  Add exception handling in the program

'''
3.	Modify your last GeoPoint program (P5) and add exception handling.
4.	Wrap the code inside the main while loop of your last program with a try block. Make sure that an error does not stop the program. The user should always have the opportunity to do another.
5.	Add three except blocks.
a.	The first will catch a TypeError exception and display “Wrong type of input!”
b.	The second will catch an exception of your choice and display a message that makes sense.
c.	The third will catch a generic Exception along with its object e and display the message “Something went wrong: “, e so that the error message e is displayed.
doAnother = 'y'
while doAnother == 'y':
    try
        …your code here…
    except TypeError :
        print "Wrong type of input!"
    except …exception you picked…  :
        print …your custom message…
    except Exception,e:
        print "Something went wrong: ", e
    doAnother = raw_input('Do another (y/n)? ') 

'''
doAnother = 'y'
while doAnother == 'y':
    try
        …your code here…
    except TypeError :
        print "Wrong type of input!"
    except …exception you picked…  :
        print …your custom message…
    except Exception,e:
        print "Something went wrong: ", e
    doAnother = raw_input('Do another (y/n)? ') 
