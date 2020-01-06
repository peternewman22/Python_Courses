"""Tools:
obj.values
obj.index
.to_dict()
Series
.isnull()
.notnull()
.name = name
.index.name
"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# note that this data type is indexed
obj = Series([3,6,9,12])
print(obj)

#printing values seperately
print(obj.values)

#printing indexes seperately
print(obj.index)

ww2_cas = Series([8700000,43000000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])

print(ww2_cas)

# calling from the index
print(ww2_cas['USA'])

# to check which countries had casualties greater than 4 million
print(ww2_cas[ww2_cas > 4000000])

# treating it as an ordered dictionary
print('USSR' in ww2_cas)

#converting a series into a dictionary
ww2_dict = ww2_cas.to_dict()

print(ww2_dict)

# convert back to a series
ww2_series = Series(ww2_dict)
print(ww2_series)