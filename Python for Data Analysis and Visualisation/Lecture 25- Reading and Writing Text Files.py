import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# default is taking the first row as a list of headers
dframe = pd.read_csv('lec25.csv',header=None)
print(dframe)

#alternative: reading tables specifying the delimeter
#dframe2 = pd.read_table('lec25.csv',sep=',',header=None)
#print(dframe2)

# indicating the specific number of rows, in this case 2
first_2_rows = pd.read_csv('lec25.csv',header=None,nrows=2)
print(first_2_rows)

#output
#dframe.to_csv('mytextdata_out.csv')

import sys
# to print output with a different separator
#dframe.to_csv(sys.stdout,sep='_')

# printing only the first three columns
dframe.to_csv(sys.stdout,columns=[0,1,2])