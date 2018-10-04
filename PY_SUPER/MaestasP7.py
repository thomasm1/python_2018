# MaestasP7
# Programmer: Thomas Maestas
# EMail: thomas76milton@gmail.com
# Purpose: File Management
'''	Use the file Countries_capitals.txt that is on BB.  Copy this information to a new file that has 20 rows. (Otherwise your list will be too big). 
a.	Create two empty list that you will use to collect the information. Something like countryList = [] and capital_list = []. 
b.	Read the information from a file. 
c.	As you read the file, split it on the ‘,’ delimiter and create two lists. Hint: Use the str.split to split on the delimiter and list.append to add to the list.
d.	 “Do a (y/n)?” loop do the following:
i.	Ask the user for a country.
ii.	Check if that country exists in the list.
iii.	Display the capital of that country (use list indexing to get the capital from the country)
'''
import sys
sys.path.append('data/Countries_capitals.txt')
import os
os.path.join('C:/wamp64/www/juillet/data/Countries_capitals.txt')

d = []
def capitals(d):
    countryList = []
    capital_list = []
    tomFile = open('C://wamp64/www/juillet/data/Countries_capitals.txt','r')
            # use Countries_capitals.txt  into file that has 20 rows
    content = tomFile.read()
    print(content)
    split ,  --> make two lists  using str.split  and list.append
    y/n loop
    ask user for country
    if country in list:
        display capital of that country[3]
    else
        print('sorry, no such file')
capitals(d)
    tomFile.close()


