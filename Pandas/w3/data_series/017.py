# Write a Pandas program to get the items which are not common of 
# two given series.

import pandas as pd

ds1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ds2 = pd.Series([3, 7, 10])

res = ds1[~ds1.isin(ds2)]