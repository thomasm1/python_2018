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
#import sys
#sys.path.append('data/Countries_capitals.txt')
import os
os.path.join('data/Countries_capitals.txt')

def capitals(country):Banner
    countryList = []
    capital_list = []
    tomFile = open('data/Countries_capitals.txt','r')
            # use Countries_capitals.txt  into file that has 20 rows
    content = tomFile.read(200)  # 200 characters to read
    words = content.split()
    print(words)
    for i in country:
        if i not in countryList:
            countryList.append(i)
            print(countryList)
            return countryList 
    if country in countryList:
        for country in countryList:
            i += 1
            print(capital_list[i])
    else:
        print('sorry, no such country on file')
    tomFile.close()

    
country = raw_input(" Please enter country of desire ... :\n---->  " )
capitals(country)


    
