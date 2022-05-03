# Write a Pandas program to create a subset of a given series based 
# on value and condition.

import pandas as pd

ds = pd.Series([1, 10, 3, 4, 20, 6, 7, 8, 9, 10])

n = 7

ds_new = ds[ds > n]