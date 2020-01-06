"""Tools:
np.sqrt()
np.random.randn(n values)
"""

import numpy as np

# make an array of 1 row, with 0 to 10
arr = np.arange(11)

# take the square root of all values (view only)
squareRootView = np.sqrt(arr)
#print(squareRootView)

# fill with 10 Random Values from a random normal distribution
A = np.random.randn(10)
# print(A)

# creating another one
B = np.random.randn(10)

        # Binary Functions
            #add
mySum = np.add(A,B)
print(mySum)
            #max compared at each pair of values
maxValue = np.maximum(A,B)
print(maxValue)
            #min compared at each pair of values
minValue = np.minimum(A,B)
print(minValue)