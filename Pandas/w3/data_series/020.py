# Write a Pandas program to display most frequent value in a given series 
# and replace everything else as ‘Other’ in the series.
import numpy as np
import pandas as pd

arr_cont = np.random.RandomState(9)
arr = arr_cont.randint(1, 10, 100)
ds = pd.Series(arr)

fr_val = ds.value_counts()

# 1
most_fr_val = fr_val[fr_val == fr_val.max()]
fr_val[fr_val != fr_val.max()] = 'Other'

# 2
# most_fr_val = fr_val[fr_val.isin([fr_val.max()])]
# fr_val[~fr_val.isin([fr_val.max()])] = 'Other'

print(fr_val)

