"""Tools:
arr.copy() --> explicitly makes a copy of an array. By default, all slices etc are VIEWS of the original array. 
"""

import numpy as np

    # this should create an array starting at zero and ending at 10, gap 1
arr = np.arange(0,11)
print(arr)
 
 
 # Calling the value at 8   
print(arr[8])

# slicing
print(arr[1:5])

# set a value over a range:
arr[0:5] = 100
print(arr)

#resetting
arr = np.arange(0,11)

#creating a slice of the array
slice_of_arr = arr[0:6]
print(slice_of_arr)

# set ALL the elements and set values
slice_of_arr[:] = 99
print(slice_of_arr)

# Keep in mind that slices of arrays etc are just VIEWS of arrays by default
print(arr)

# to make a copy
arr_copy =arr.copy()

#now indexing in 2d array...
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

# to pull up the first row... which the first entry in the 2d array
print(arr_2d[0])

# to pull up individal values

print(arr_2d[0][0]) # the first value is the row, the 2nd is the column

#2d array slicing to get the top right hand 2x2 array
# we want rows up to the 3rd row and excluding the first column

print(arr_2d[:2,1:])

# fancy indexing

arr2d = np.zeros((10,10))
print(arr2d)
arr_length = arr2d.shape[1]
print(arr_length)

# I predict that this should produce an array of 10 columns and 10 rows, rows progressing from 0 by 1 each time
for i in range(arr_length):
    arr2d[i] = i
    
print(arr2d) # and I was correct!

# Now we can select individual rows in any order we choose
arr2d[[2,4,6,8]]