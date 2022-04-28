# Write a Pandas program to compare the elements of the two Pandas Series.

# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

print(ds1 == ds2)

print(ds1 > ds2)

print(ds1 < ds2)
