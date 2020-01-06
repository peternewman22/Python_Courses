import numpy as np
from pandas import Series, DataFrame
import pandas as pd

my_ser = Series([1,2,3,4],index=['A','B','C','D'])

print(my_ser)
#calls the index
my_index = my_ser.index

# Index are immutable
print(my_index[2:])

