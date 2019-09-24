from numpy import matrix
import numpy as np 

aa = matrix([[2,3],[2,1]])
bb = matrix([[3,1],[1,1]])
print('a:\n{}'.format(aa))
print('b:\n{}'.format(bb))

# arithmetic operators on arrays applied elementwise. 
# new array is filled and returned with the result.

#  2 arrays a and b, and subtract b from a:
# can NOT do such an operation with arrays of differnt sizes, 
# you'll get an error
a = np.array( [20,30,40,50] )
b = np.array( [0, 1, 2, 3] )
c = a - b
c = [20, 29, 38, 47]
print(c)
print()
# You can also perform scalar operations elementwise on the entire array
b**2
b = [0, 1, 4, 9]
print(b)
print()

# Or even apply functions
10*np.sin(a)
a = [ 9.12945251, -9.88031624,  7.4511316 , -2.62374854]

#  operation between arrays are applied elementwise
a = np.array( [20,30,40,50] )
b = np.array( [0, 1, 2, 3] )
c = a * b
c = [0, 30, 80, 150]
print(c)
print()

# functions 
a = np.array( [20,30,40,50] )
a.max() # 50
a.min() # 20
a.sum() # 140

# multi-dimensional array: "axis" parameter
b = np.arange(12).reshape(3,4)
b = [[ 0,  1,  2,  3],
     [ 4,  5,  6,  7],
     [ 8,  9, 10, 11]]

# b.sum(axis=0) # [12, 15, 18, 21]
# b.min(axis=1) # [0, 4, 8]
# b.cumsum(axis=1) # [[ 0,  1,  3,  6], [ 4,  9, 15, 22], [ 8, 17, 27, 38]]
 
b = np.arange(3)
b = [0, 1, 2]

np.exp(b) # [ 1.0, 2.71828183, 7.3890561 ]
np.sqrt(b) # [ 0.0 ,  1.0, 1.41421356]
np.floor(np.exp(b)) # [ 1.0, 2.0, 7.0 ]
np.round(np.exp(b)) # [ 1.0, 3.0, 7.0 ]

#   arrays indexed, sliced and iterated  
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[2] # 2
a[2:5] # [2, 3, 4]
a[-1] # 10
a[:8] # [0, 1, 2, 3, 4, 5, 6, 7]
a[2:] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
print()
#   multi-dimensional arrays 
b = [[ 0,  1,  2,  3],
     [10, 11, 12, 13],
     [20, 21, 22, 23],
     [30, 31, 32, 33],
     [40, 41, 42, 43]]
print(b)
print()
# b[2,3] # 23
# b[0:5, 1] # each row in the second column of b --> [ 1, 11, 21, 31, 41]
# b[ : ,1] # same thing as above --> [ 1, 11, 21, 31, 41]
# b[1:3, : ] # each column in the second and third row 
#            # of b --> [[10, 11, 12, 13], [20, 21, 22, 23]]

# Iterating over multidimensional arrays with respect to the first axis
for row in b:
  print(row)
# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]

