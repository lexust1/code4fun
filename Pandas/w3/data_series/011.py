# Write a Pandas program to sort a given Series.

import pandas as pd

ds = pd.Series(['1', '2', '20', '40', 'python', 'eleven', '4', '@symbol'])

new_ds = ds.sort_values()

