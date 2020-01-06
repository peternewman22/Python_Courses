import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import json

# Note: this code won't run
json_obj = "something or rather"
data = json.loads(json_obj)

# converting back
json.dumps(data)

# importing into data
dframe = 