import numpy as np
import pandas as pd
from pandas import Series,DataFrame

"""
# creating 2 series with different indexes
ser1 = Series([0,1,2],index=['A','B','C'])
print(ser1)
ser2 = Series([3,4,5,6],index=['A','B','C','D'])
print(ser2)

# adding these together we find where the indexes don't match
print(ser1 + ser2)
"""
# creating 2 different sized dataframes
# NB: list('AB') takes that list and makes a list of it
dframe1 = DataFrame(np.arange(4).reshape((2,2)),columns=list('AB'),index=['NYC','LA'])
print(dframe1)

# making a 3x3 dataframe
dframe2 = DataFrame(np.arange(9).reshape((3,3)),columns=list('ADC'),index=['NYC','SF','LA'])
print(dframe2)

# if we add these together, I predict that it will add the similar indexes and NaN the others
print(dframe1 + dframe2)
# it doesn't, and that's because the row and columns index matched

# to replace the null values, call .add and fill_value
print(dframe1.add(dframe2,fill_value=0))
# not really following exactly what's going on here. Data seems to have been preserved

ser3 = dframe2.ix[0]
print(dframe2-ser3)

