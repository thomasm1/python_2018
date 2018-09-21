from itertools import permutations

subjects = ('Maths', 'Programming', 'Biology')
arrangements = permutations(subjects, 3)
print(arrangements)
#<itertools.permutations object at 0x10ac52780>

#i.e. n!/ (n - k)!
from scipy.special import factorial
n= 26
k= 8
print(factorial(n)/factorial(n - k))
# 76030000000.000000014
from string import ascii_lowercase as lowercase
from itertools import permutations

things = permutations(lowercase, 8)
print(len(things))
