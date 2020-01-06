import numpy as np
import pandas as pd
from pandas import Series,DataFrame
"""
data = Series(['one','two',np.nan,'four'])
print(data)

#finding the missing values
missing_values = data.isnull()
print(missing_values)

#drop missing values
drop_missing_values = data.dropna()
print(drop_missing_values)

#Just for my own interest: re-indexing... gotta remember that each thing is a VIEW
drop_reindex = drop_missing_values.reset_index(drop=True)
print(drop_reindex)

# now working with DataFrames
dframe = DataFrame([[1,2,3],[np.nan,5,6],[np.nan,np.nan,np.nan]])
print(dframe)

# to drop the null values --> unforunately drops the entire row
clean_dframe = dframe.dropna()
print(clean_dframe)

# to just drop completely NaN rows
drop_NaN_row = dframe.dropna(how='all')
print(drop_NaN_row)

#to drop columns with null values, use the axis = 1
no_NaN_col = dframe.dropna(axis=1)
print(no_NaN_col) """

# declare a shortcut for NaN
npn = np.nan
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
#print(dframe2)

#threshod by number of values: drops rows with under 2 values
two_data_points_only  = dframe2.dropna(thresh=2)
print(two_data_points_only)

#threshold of 3
three_points_only = dframe2.dropna(thresh=3)
print(three_points_only)

# fill the NaN values
fill_NaN = dframe2.fillna(1)
print(fill_NaN)

#fill by different columns using a dictionary
fill_by_cols = dframe2.fillna({0:0,1:1,2:2,3:3})
print(fill_by_cols)

#to modify existing object: use inplace=True as an argument in fillna
