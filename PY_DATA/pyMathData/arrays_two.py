import numpy as np 

# https://docs.scipy.org/doc/numpy/reference/index.html
#

np.int64 # Signed 64-bit integer types
np.float32 # Standard double-precision floating point
np.complex # Complex numbers represented by 128 floats
np.bool # Boolean type storing TRUE and FALSE values
np.object #   object type
# np.string # Fixed-length string type
np.unicode # Fixed-length unicode type

###  compared directly 
print('a = np.array([1, 2, 3])')
a = np.array([1, 2, 3])
print(a)
print('b = np.array([5, 4, 3])')
b = np.array([5, 4, 3])
print(b)

print('compare directly: boolean value for each element') 
# compare directly: boolean value for each element
print('a == b')
print(a == b) # array([False, False, True])
a <= 2 # array([False, True, True]) 
print()

#  compare the entire arrays
np.array_equal(a, b) # False

# sort by axis
print('sort by axis') 
print('np.array([[2, 4, 8], [1, 13, 7]])')
c = np.array([[2, 4, 8], [1, 13, 7]])
c.sort(axis=0) # array([[1, 4, 7], [2, 13, 8]])
c.sort(axis=1) # array([[2, 4, 8], [1, 7, 13]])
print()

print('Array manipulation')
### Array manipulation 

# Transposing array
print('Transposing array')
d = np.transpose(c)
print()
print()

print('Changing array shape')
# Changing array shape
c.ravel() # This flattens the array
c.reshape((3, 2)) # Reshape the array from (2, 3) to (3, 2)
print()
print()

# Adding and removing elements 
print('Adding and removing elements ')
append = np.append(c, d)
print(append) # Append items in array c to array d
insert = np.insert(a, 1, 5, axis=0) # Insert the number '5' at index 1 on axis 0
print(insert)
#np.delete(a,[1], axis=1) # Delete item at index 1, axis 1
print()

# Combining arrays
# np.concatenate((c,d),axis=0)  # Concatenate arrays c and d on axis 0
# np.vstack((c,d),axis=0)  # Concatenate arrays c and d vertically (row-wise)
# np.hstack((c,d),axis=0)  # Concatenate arrays c and d horizontally (column-wise)