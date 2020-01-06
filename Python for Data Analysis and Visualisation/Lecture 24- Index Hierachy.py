import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

# You can have multiple index levels, the second index is a subindex
ser = Series(randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
print(ser)

#checking multiple levels

ix_lvls = ser.index
print(ix_lvls)

#print major point 1
lvl1 = ser[1]
print(lvl1)

#print major point 2
lvl2 = ser[2]
print(lvl2)

#print inner: argument1: both outer levels, argument 2: inner level 'a'
a_both = ser[:,'a']
print(a_both)

# creating DataFrames from multiple levels, lower = columns, upper = rows
dframe = ser.unstack()
print(dframe)

# constructing a dataframe with multiple index levels

dframe2 = DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],
            columns=[['NY','NY','LA','SF'],['cold','hot','hot','cold']])
print(dframe2)

# naming the index levels
dframe2.index.names = ['INDEX_1','INDEX_2']
dframe2.columns.names = ['Cities','Temp']
print(dframe2)

# interchange the level orders: swap cities and temp, swapping columns
#dframe2 = dframe2.swaplevel('Cities','Temp',axis=1)
#print(dframe2)

#sort by level 1: 'a','b'
dframe2.sortlevel(0)

# sort by level 2: 1,1,2,2
print(dframe2.sortlevel(1))

# arithmetic on the columns
sum_cols = dframe2.sum(level='Temp',axis=1)
print(sum_cols)