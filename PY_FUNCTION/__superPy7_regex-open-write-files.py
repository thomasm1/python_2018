#REGEX SYMBOLS
# -*- coding: utf-8 -*-
'''
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets
#
#Now instead of a hard-to-read regular expression like this:


phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')
you can spread the regular expression over multiple lines with comments like this:

'''

#phoneRegex = re.compile(r'''(
'''
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
'''
#    )''', re.VERBOSE)


'''
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].strisdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
print('505-508-7707 is a phone number:')
print(isPhoneNumber('505-508-7707'))
print('mush mush is a phone number:')
print(isPhoneNumber('mush mush'))
'''

'''
msg = "Call me at 333-333-3333 tomorrow"
for i in range(len(msg)):
    chunk = msg[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

'''
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 222-222-2222.')
#pile(r'Agent \w+')
#print namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

######## chapter 8  ###########
print
print '# CHAPTER 8 Read Write Files'
#\\\\\ in windows and ///// OSX and Linux
import sys
sys.path.append('data/Stock_list.csv')

import os
os.path.join('usr', 'bin', 'spam')
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:/Users/tmaestas', filename))
print
os.getcwd()
# os.chdir('C:\\Windows\\System32')
os.getcwd()
#create new folders METHOD
os.makedirs
os.makedirs('C:/delicious/walnut/w/waffles2')

#Opening Files
#helloFile = open('/Users/pi/hello.txt')
#sonnetFile = open'sennet29.txt')

#Writing to Files
tomFile = open('C:/delicious/walnut/w/waffles2/t.txt', 'w')
tomFile.write('Hellow wolrd\n')
tomFile.close()
tomFile = open('C:/delicious/walnut/w/waffles2/t.txt')
content = tomFile.read()
tomFile.close()
print(content)
