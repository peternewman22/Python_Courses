import numpy as np
import pandas as pd
from pandas import Series, DataFrame
"""
ser1= Series(range(3),index=list('CAB'))
print(ser1)

#calling the sort function: sort by index
print(ser1.sort_index())

#to call a sort based on values
print(ser1.order())"""

"""
from numpy.random import randn
# Ranking
ser2 = Series(randn(10))
print(ser2)

# to sort by rank
print(ser2.order())

# call rank: sorting/ordering works by putting the rank in order from smallest to largest
print(ser2.rank())
"""
from numpy.random import randn
ser3 = Series(randn(10))
print(ser3)

print(ser3.rank())
ser3.sort()
print(ser3.rank())