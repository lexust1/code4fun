# Write a Pandas program to convert a NumPy array to a Pandas series
# Sample NumPy array: d1 = [10, 20, 30, 40, 50]

import numpy as np
import pandas as pd

np_arr = np.array([10, 20, 30, 40, 50])

ds = pd.Series(np_arr)

print(np_arr)
print(ds)