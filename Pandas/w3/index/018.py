# Write a Pandas program to get the index of an element of a given Series.

import pandas as pd

ds = pd.Series([1, 3, 5, 7, 9, 11, 13, 15], index=range(0, 8))
print(ds)

print(ds[ds == 9].index[0])
      