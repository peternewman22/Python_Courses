""" Tools: 
Numpy
numpy.array(tuple)
array.shape --> rows, columns
array.dtype
numpy.zeros(shape, dtype=float, order='C')
numpy.ones(shape, dtype=None, order='C')[source]
numpy.empty(shape, dtype=float, order='C')
numpy.eye(N, M=None, k=0, dtype=<type 'float'>)
numpy.arange([start, ]stop, [step, ]dtype=None)
"""

import numpy as np

# You can parse a list as an object

myList = [1,2,3,4]

myArray1 = np.array(myList)

#print myArray1


# you can then quickly make a multi-dimensional array from tuples or lists of lists

myList2 = [11,22,33,44]

myList3 = [111,222,333,444]

myLists = [myList, myList2, myList3]

myArray2 = np.array(myLists)

#print myArray2
#print myArray2.shape

# We can check the TYPE of the array using dtype
#print myArray2.dtype

# Make a list of zeros, default floating type

zeros1 = np.zeros([5,5])
#print zeros1

# Make an array of 1s, default floating type

ones1 = np.ones([5,5]) 
#print ones1

# Make an empty matrix

empty1 = np.empty(5)
#print empty1

# Make an identity matrix

identityMatrix = np.eye(5)
#print identityMatrix

# Make an evenly spaced list, starting at 3, ending at 50 and going up by 4's

myArray3 = np.arange(3,50,4)
#print myArray3