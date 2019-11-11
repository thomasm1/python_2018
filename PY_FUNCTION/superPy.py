print(" Python!  3.6")
how_many_snakes = 1
snake_string = """
Welcome to the Great 
Python3 Featurette!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, __TMM__TMM__TMM__
"""
print(snake_string)
'''
FUNCTIONS
cmp(x, y) #Compares two values
len(seq) #Returns the length of a sequence
list(seq) #Converts a sequence to a list
max(args) #Returns the maximum of a sequence or set of arguments
min(args) #Returns the minimum of a sequence or set of arguments
reversed(seq) #Lets you iterate over a sequence in reverse
sorted(seq) #Returns a sorted list of the elements of seq
tuple(seq) #Converts a sequence to a tuple
d = {}
d.clear()
d.copy()
d.deepcopy()
#
{}.fromkeys(['name', 'new']) 
print d['name']  == print d.get('name')
d.setdefault('name', 'n/a')
#
d = {'name':'0'}
x = {'name':'new'}
d.update(x)
#
{'name': 'new'}
>>> x
'''
# ######  MATRIX GET
new_matrix = {(0,1): 'justin', (1,0): 'kelli', (2,2):'paul'}
print (new_matrix.get((0,1), "None"))
print (new_matrix.get((2,0), "None"))
'''
justin
None
'''
print('###')
#  #########  DICTIONARY MAKE
d={}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
'''
{'age': 42, 'name': 'Gumby'}
'''
print('###')
#
xs = range(1,6)
print (xs)
'''
[1, 2, 3, 4, 5]
'''
print('###')
#
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
print('###')
#
print ('\n')
flowers = {'rose': 'Floribunda', 'lily': 'daylily'}
print(flowers)
'''
print  ("My favorite flower is % (rose)s." %flowers)
print("My favorite flower is % (rose)s." %flowers)
'''
print('###')
#
for k, v in flowers.items():
     print (k, v)
'''
rose Floribunda
lily daylily
lily daylily
rose Floribunda
'''
print('###')
#
for k in sorted(flowers):
    print (k, flowers[k])

list1 = ['a', 'b']
list2 = ['solstice', 'wildfire']
for f in range(len(list1)):
    print (list1[f], 'is a', list2[f])
'''
a is a solstice
b is a wildfire
'''
print('###')
#
from math import sqrt
for n in range(64, 0, -1):
    print (sqrt(n))
    break
'''
8.0  ...and without break
8.0
7.937253933197.87400787401
[until reaching 1]
'''
print('###')
#
a = 'fish'
b = range(3)
for x, y in zip(a,b):
    print (x, y)
'''
f 0
i 1
s 2
'''
print('###')
#
for r, v in zip(list1, list2):
    print (r, 'is a', v)
''' 
a is a solstice
b is a wildfire
'''
print('###')

