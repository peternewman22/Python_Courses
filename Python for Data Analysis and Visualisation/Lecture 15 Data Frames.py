"""Tools:
pd.read_clipboard()

"""


import numpy as np
import pandas as pd

from pandas import Series,DataFrame

import webbrowser
websites = 'https://en.wikipedia.org/wiki/NFL_win-loss_records'
# webbrowser.open(websites)

nfl_frame = pd.read_clipboard()

#print(nfl_frame)
#once we have the columns, we can grab those from the columns
#print(nfl_frame.columns)

#grabbing multiple columns to create a view data frame
view1 = DataFrame(nfl_frame,columns=['Team','First Season','Total Games'])
#print(view1)

# retrieving rows, put a number in head = first 5 rows by default
#print(nfl_frame.head())

last_5_rows_View = nfl_frame.tail()

#third_row = nfl_frame.ix[2]
#print(third_row)

# To assign values to a whole column...that we don't yet have...
nfl_frame['Stadium']="Levi's Stadium"
#print(nfl_frame)

# to attach an array of numbers to the last column...
nfl_frame['Stadium']=np.arange(5)
#print(nfl_frame)

# Add a series to a dataframe... create a data frame

stadiums = Series(["Levi's stadium","AT&T stadium"],index=[4,0])
#print(stadiums)

#insert into dataframe
nfl_frame['Stadium'] = stadiums
#print(nfl_frame)

#delete entire columns
del nfl_frame['Stadium']
#print(nfl_frame)

# using dictionaries
data = {'City':['SF','LA','NYC'],'Population':[123,1231,12315]}

city_frame = DataFrame(data)
print(city_frame)

