import numpy as np
import pandas as pd
from pandas import Series,DataFrame



dictionary = dict(zip(Codes, Descriptions))

toReplace = pd.read_clipboard()

print(toReplace.columns)

listToReplace = toReplace["Topic"].tolist()

for x in listToReplace:
    if x in dictionary:
        x = dictionary[x]
        print(x)
    else: print(x)

    




