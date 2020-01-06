import numpy as np
import pandas as pd

from pandas import Series,DataFrame
"""
# make a series
ser1 = Series(np.arange(3),index=['A','B','C'])

ser1 = 2*ser1

print(ser1)

# to select the second row, we can either use the Index:
print(ser1['B'])
print(ser1[1])

#grab sections by index
print(ser1[0:3])

# grab by multiple indexes
print(ser1[['A','B']])

# grab by logic
print(ser1[ser1>3])

# we can also set values with this method
ser1[ser1>3]=10
print(ser1)

"""

# now applying everthing to a DataFrame
dframe= DataFrame(np.arange(25).reshape((5,5)),index=['NYC','LA','SF','DC','Chi'],
columns=['A','B','C','D','E'])

print(dframe)

# calling by column
print(dframe['B'])

#select more than one column
print(dframe[['B','E']])

# logic selecting rows:
print(dframe[dframe['C']>8])

# printing boolean values
print(dframe>10)

# using ix to print from the rows index
print(dframe.ix['LA'])

# we can also use the index number
print(dframe.ix[1])