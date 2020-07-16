# Bitcoin_Data_Scraper
# Unknown Data Types/Structures

import numpy as np

# 1. 
# if contents of the initial array not known,  
# initialize to use it later. 
print('1. if contents of the initial array not known initialize to use it later')

# list or tuple array type
print('list or tuple array type')
np_array1 = np.array([[ 0,  1,  2,  3,  4],
                     [ 5,  6,  7,  8,  9],
                     [10, 11, 12, 13, 14]])
print(np_array1)
print()

np_array2 = np.array([(1.5,2,3), (4,5,6)], dtype=float)
print(np_array2)
print()

# 3x4 array of 0's
print('3x4 array of 0')
z = np.zeros((3,4))
print(z)
print()

# 2x3x4 array of int 1
print('2x3x4 array of int 1')
o = np.ones((2,3,4), dtype=np.int16) 
print(o)
print()

# empty 2x3 array
print('empty 2x3 array')
np.empty((2,3))
print()

# 1D array of numbers from 10 to 30 in increments of 5
print('1D array of numbers from 10 to 30 in increments of 5')
i = np.arange( 10, 30, 5 )
print(i)
print()

# 1D array of numbers from 0 to 2 in increments of 0.3
print('1D array of numbers from 0 to 2 in increments of 0.3')
ii = np.arange( 0, 2, 0.3 ) 
print(ii)
print()

# 1D array of 9 numbers equally spaced from 0 to 2 
print('1D array of 9 numbers equally spaced from 0 to 2')
l = np.linspace( 0, 2, 9 ) 
print(l)
print()

# 2. 
# Get Axes, dimensions, total number of elems ### 
print('2. Get Axes, dimensions, total number of elems')

# Get # of axes (dimensions)
print('Get num of axes (dimensions)')
ndim = np_array1.ndim
print(ndim)
print()

# Gets the dimensions of the array
print('Gets the dimensions of the array')
shape = np_array1.shape
print(shape)
print() 

# (product --i.e., total number, of all elements # in np_array.shape)
print('product --i.e., total number, of all elements # in np_array.shape')
size = np_array1.size
print(size)
print()

# Describe the type of the elements in the array
print('Describe the type of the elements in the array')
dtype = np_array1.dtype
print(dtype)
print()

