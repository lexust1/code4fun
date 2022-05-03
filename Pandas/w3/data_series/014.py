# Write a Pandas program to change the order of index of a given series.

import pandas as pd

ds = pd.Series(data=[10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])

ds_new = ds.reindex(index=['B', 'E', 'A', 'C', 'D'])

print(ds)
print(ds_new)

