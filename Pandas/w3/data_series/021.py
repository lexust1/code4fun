# Write a Pandas program to find the positions of numbers 
# that are multiples of 5 of a given series.

import numpy as np
import pandas as pd

ds = pd.Series([0, 10, 11, 13, 15, 20, 21])

res = np.where(ds % 5 == 0)

print(res)
