#  Dictionaries
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
spam = {'species': 'cat', 'name': 'Zophie', 'age': '8'}
print eggs == spam

birthdays = {'Alice': 'Apri 1', 'Bob': 'Dec 123', 'Carol': 'Mar4'}
'''
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updatlupe sed.')   # QQQ: prog does not break out
'''

#Keys
spam = {'color': 'red', 'age': 42}
print spam.keys()
print('')

for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
print('')

picnicItems = {'apples': 5, 'cups': 2}
print ('Im bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
if 'color' not in spam:
    spam['color'] = 'black'
spam.setdefault('color', 'black')
print('')
#

# ---0-1-2-
# ----------
# 0| 0 1 0
# 2| 3 0 0
# 2| 0 0 2
#----------
'''
s_matrix = {(0,1):1, (1,0):3, (2,2):2}
s_matrix[(0,1)]
s_matrix.get((0,2),1) 
print(s_matrix.get((0,2),1))
print(s_matrix.get((0,2),2))
print(s_matrix.get((1,0),5))
print '\n'
'''
# __________
new_matrix = {(0,1): 'justin', (1,0): 'kelli', (2,2):'paul'}
print new_matrix.get((0,1), "None")
print new_matrix.get((2,0), "None")
# __________
print '\n'
flowers = {'rose': 'Floribunda', 'lily': 'daylily'}
'''  print  "My favorite flower is % (rose)s." %flowers
print("My favorite flower is % (rose)s." %flowers) '''

#userInput = input('enter input ')
#while userInput <= 5:
#    print userInput
#    break
for k, v in flowers.items():
     print k, v
'''
rose Floribunda
lily daylily
lily daylily
rose Floribunda
'''
for k in sorted(flowers):
    print k, flowers[k]

list1 = ['a', 'b']
list2 = ['solstice', 'wildfire']

for f in range(len(list1)):
    print list1[f], 'is a', list2[f]
'''
a is a solstice
b is a wildfire
'''
from math import sqrt
for n in range(64, 0, -1):
    print sqrt(n)
    break
'''
8.0  ...and without break
8.0
7.937253933197.87400787401
[until reaching 1]
'''
 
a = 'fish'
b = range(3)
for x, y in zip(a,b):
    print x, y
'''
f 0
i 1
s 2
'''
for r, v in zip(list1, list2):
    print r, 'is a', v
''' 
a is a solstice
b is a wildfire
'''
xs = range(1,6)
print xs
'''
[1, 2, 3, 4, 5]
'''
total = 1
for x in xs:
    total = total +1
    print(total)
'''
2
3
4
5
6
'''


print('#STRINGS')
#
import pprint
message = "who dis? And where is the train going..."
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character]= count[character] + 1
pprint.pprint(count)

print('# TIC-TAC-TOE')
theBoard = {
            'top-L': 'X',  'top-M': '0',  'top-R': '',
            'top-L': '0',  'top-M': 'X',  'top-R': '',
            'top-L': ' ',  'top-M': '0',  'top-R': 'X'
            }
#def printBoard(board):            
#   print(board['top-L'] = '|' = board['top-M'] + '|' _-                    
 


raw_string = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title': 'TMM', 'text': 'Well, Hello World'}
print raw_string % data

print('\n# IN & OUT OPERATORS')
'p' in 'python'
python = 'Python'
python = python.upper()
print python

'''
# INPUT
print('how are you today?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('Chin up!')

#isX STRING METHODS

while True:
    print('Select a new password (letters and numbers only:')
    password = input()
    if password.isalnum():
        print('Great, password saved!!'Passwords can only have letters and numbers.')
'''
print('\n#  join() METHODS')
print(', '.join(theBoard))
print(', '.join(['cats', 'bats', 'Tom']))
print(' '.join(['Mi', 'nombre', 'es', 'Tom','likes','.join()']))
print '_tmm_'.join(['My','name', 'jis', 'Tom'])

print('\n#  split() METHODS')
paragraph = '''Dear Mayor,
Firstly, thank you for your audience.
Secondly, I am a concerned citizen. Our city of Albuquerque has grown to violent!
Therefore, I ask for better education programs to distract idle, unemployed hands.
Thank you'''
print(paragraph.split('/n'))
print '#'
print(paragraph.split())
print'#'
print('1.My name is Tom'.split())
csv_split = '2.d3.string.file.My.name.is.Tom.and.this.is.split()'.split('.')
print (csv_split) 

print('\n#  split() and join() METHODS')
csv_split = ('3,source,target,My,name,is,Tom,and,this,is,a,csv,formatted,list'.split(','))
print(csv_split) 
print('.'.join(csv_split))

print('\n#  ljust() rjust() and center() STRING METHODS')
'Hello'.center(20)
'Hello'.center(20, '=')
'Hello'.rjust(10)
def inventory(itemsDict, leftWidth, rightWidth):
    print('INVENTORY ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
inventoryItems = {'item1': 3, 'item2': 32, 'item3':44}
inventory(inventoryItems,12,5)
inventory(inventoryItems,20,6)

print('\n#  strip() rstrip() and lstrip() REMOVING WHITESPACE METHODS')
spam = '    Hellow Thar   '
print(spam)
print(spam.lstrip())

print('')
print('## notes1250 below:')
d = {'key1': 'value1', 'key2':'value2'}
key,value = d.popitem()
print(key)
print(value)
import math
y = math.pow(2,3)
x =y
print(x)
print(y)
x = 3
print(x)
x += 2
print(x)
print('#Conditionals')
#name = raw_input('ask a question : ')
name = "who?"
if name.endswith(' ? '):
    print('Hellow @@withstrip')
if name.endswith('?'):
    print('Hellow nostrip')
print("Type age guess >>>assert 0 > age > 100, ")
#age = raw_input('enter age : ')
print('')
print('# FORMATTING')
format = "Pi with three decimals: %.3f"
from math import pi
print(format % pi)
print('')
format = "Hello, %s, %s enough for you?"
values = ('Person', 'Cool')
print(format % values)
print('#FIND METHOD')
print('stringinginginginginging'.find('tr'))
print('tomcat tomtom tomcattom'.find('cat', 7,15))
print('#Other string methods: rfind(), index(), rindex(), count(), startswith(), endswith()')
sequence = ['1','2','3','4','5']
separation = '.'
print(separation.join(sequence))
 
dirs = ('', 'usr', 'bin', 'env')
print('/'.join(dirs))
print('Tom Maestas'.lower())
fname = 'Tom'
if fname in ['tom', 'maestas','MA']:
    print('Found it')
elif fname.lower() in ['tom', 'maestas','MA']:
    print('Found it 2')
print('This is a test'.replace('is','eeeez'))

print('')
how_many_snakes = 1
snake_string = """Welcome to Tom's program! 
             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/
 
"""
print('The Above presented on October 6' + snake_string * how_many_snakes)


