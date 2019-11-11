print('Python Scratchpad File')
print('''
Built-in Functions-->Standard Library, eg.min(list), len()
Standard modules (functions): sys, os, pprint
https://pymotw.com/3/
https://pymotw.com/2/
''')
print('week 3')
# Indexing, Slicing, Adding lists, Empty lists
number = [3,4,5,6,7,8]
number[0:6:2]
print(number[0:6:2])
print
list1=['white', 'yellow', 'pink', 'red']
lillies=['daylily', 'waterlily', 'asiatic']
flowers=[list1+lillies]
print(flowers)
print('daylily' in flowers) 
print('daylily' in lillies)
print
list1.append('patiorose')
print(flowers)
print(list1)
flowers=[list1+lillies]
print(flowers)
print
emptylist = []
print(emptylist)
print
print(list1.count('waterlily'))
print(lillies.count('waterlily'))
print(flowers.count('waterlily'))
flowers=[list1+lillies]
print(flowers.count('waterlily'))
list1.extend(lillies)
print(list1.count('waterlily'))
print 
s = "hello world"
s.find('llo')
s.find('eee')
print(s.find('eee'))
s.find('llo',14,18)
llo = s.find('llo',14,18)
print(s.find('llo',14,18))
print(llo)
#######################33
 #  Sept 20, 2017
print '\n'
greeting = "bonjour"
print "hello", '\n', greeting
print 'hello', '\n-----\n', greeting
print '\n'
#
how_many_snakes = 1
snake_string = """
Welcome to Tom's program! 
             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/
 
"""
print('The Above presented on October 16' + snake_string * how_many_snakes)

