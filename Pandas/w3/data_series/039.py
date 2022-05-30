# Write a Pandas program to find the index of the first occurrence of 
# the smallest and largest value of a given series.

import pandas as pd

ds = pd.Series([0, 1, 2, 10, 15, -5, 10, -5, -3, 15, 21, 21, 17, 21])

idx_of_max = ds.idxmax()
idx_of_min = ds.idxmin()
