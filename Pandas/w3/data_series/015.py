# Write a Pandas program to create the mean and standard deviation of 
# the data of a given Series.

import pandas as pd

ds = pd.Series([10, 20, 30, 40, 400, 500, 60, 900, 1000])

ds_mean = ds.mean()
ds_std = ds.std()

print(ds_mean)
print(ds_std)
