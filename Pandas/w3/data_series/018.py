# Write a Pandas program to compute the minimum, 25th percentile, 
# median, 75th, and maximum of a given series.

import pandas as pd
import numpy as np

arr_cont = np.random.RandomState(10);

arr = arr_cont.normal(0, 1, 100)

ds = pd.Series(arr)

ds_0 = ds.quantile(0)
ds_25 = ds.quantile(0.25)
ds_50 = ds.quantile(0.5)
ds_75 = ds.quantile(0.75)
ds_100 = ds.quantile(1) 

ds_all = ds.quantile([0, 0.25, 0.5, 0.75, 1])

ds_min = ds.min()
ds_max = ds.max()