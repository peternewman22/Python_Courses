"""Tools:
arr.T is the transpose
dot product"""
import numpy as np

# make a matrix of 50 values, ordered across the rows, 10 rows by 5 columns
arr = np.arange(50).reshape((10,5))
print(arr)

arr = arr.T
print(arr)

#making a 3d array
arr3d = np.arange(50).reshape((5,5,2))
print(arr3d)

# transpose a 3d matrix, specifying the axis
print(arr3d.transpose(1,0,2))

#swap axis explicitly
# arr.swapaxis()


