# Write a Pandas program to get the positions of items of a given series 
# in another given series.

import pandas as pd

ds1 = pd.Series([0, 1, 10, 20, 30, 35, 40, 45, 50, 70])
ds2 = pd.Series([0, 1, 30, 8])

print(list(ds1[ds1.isin(ds2)].index))

