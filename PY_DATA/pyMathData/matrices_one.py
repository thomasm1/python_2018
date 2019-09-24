
import numpy as np 

np.int64 # Signed 64-bit integer types
np.float32 # Standard double-precision floating point
np.complex # Complex numbers represented by 128 floats
np.bool # Boolean type storing TRUE and FALSE values
np.object #   object type
# np.string # Fixed-length string type
np.unicode # Fixed-length unicode type

### Numpy arrays can actually be compared directly just like the arithmetic

a = np.array([1, 2, 3])
b = np.array([5, 4, 3])

# If we compare directly we get a boolean value for each element
a == b # array([False, False, True])
a <= 2 # array([False, True, True])

# If we want to compare the entire arrays, we can use Numpy's built in function
np.array_equal(a, b) # False

# We can sort by axis
c = np.array([[2, 4, 8], [1, 13, 7]])
c.sort(axis=0) # array([[1, 4, 7], [2, 13, 8]])
c.sort(axis=1) # array([[2, 4, 8], [1, 7, 13]])

### Array manipulation is also easy with Numpy built in functions

# Transposing array
d = np.transpose(c)

# Changing array shape
c.ravel() # This flattens the array
c.reshape((3, 2)) # Reshape the array from (2, 3) to (3, 2)

# Adding and removing elements 
np.append(c, d) # Append items in array c to array d
np.insert(a, 1, 5, axis=0) # Insert the number '5' at index 1 on axis 0
$np.delete(a,[1], axis=1) # Delete item at index 1, axis 1

# Combining arrays
np.concatenate((c,d),axis=0)  # Concatenate arrays c and d on axis 0
np.vstack((c,d),axis=0)  # Concatenate arrays c and d vertically (row-wise)
np.hstack((c,d),axis=0)  # Concatenate arrays c and d horizontally (column-wise)