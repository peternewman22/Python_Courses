import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib
"""
# create a dataframe
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1= DataFrame(arr,index=list('AB'),columns=["One","Two","Three"])
print(dframe1)

# add up the values from each column, ignore NaN values
sum_by_Cols = dframe1.sum()
print(sum_by_Cols)

# sum by rows
sum_by_Rows = dframe1.sum(axis=1)
print(sum_by_Rows)

#finding the minimum value by cols
min_value = dframe1.min()
print(min_value)

#finding the index of the minimum value
index_min_value = dframe1.idxmin()
print(index_min_value)

#accumulation sum
accumulation_cols= dframe1.cumsum()
print(accumulation_cols)

#summary statistics
mySummary = dframe1.describe()
print(mySummary)
#calculating the covariance


import pandas.io.data as pdweb

import datetime

# import from yahoo stock data
prices = pdweb.get_data_yahoo(['CVX','XOM','BP'],
    start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Adj Close']

print(prices.head())

#finding the volume

volume = pdweb.get_data_yahoo(['CVX','XOM','BP'],
    start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Volume']    

print(volume.head())

# finding the returns: percent change on the stock
rets = prices.pct_change()
print(rets.head())

# finding the correlation of the stocks
corr = rets.corr
print(corr)

# now plotting the stocks
prices.plot()

# plotting library
import seaborn as sns
import matplotlib.pyplot as plt

sns.corrplot(rets,annotation=False,diag_names=False)
"""

# check for unique values
ser1 = Series(['w','x','w','y','x'])
print(ser1)
set_ser1 = ser1.unique()
print(set_ser1)

#count the values
ser1_count = ser1.count()
print(ser1_count)

# return count of individual values
ser1_value_count = ser1.value_counts()
print(ser1_value_count)



