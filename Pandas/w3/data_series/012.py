# Write a Pandas program to add some data to an existing Series.

import pandas as pd

ds = pd.Series([1, 2, 3, 40, 50, 60, 80, '20'])

new_ds = ds.append(pd.Series(['eleven', 'python']))

new_ds2 = pd.concat([ds, pd.Series(['eleven', 'python'])])

print(new_ds)
print(new_ds2)