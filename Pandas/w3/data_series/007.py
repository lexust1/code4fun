# Write a Pandas program to change the data type of given a column or a Series.

# Sample Series:
    
# Original Data Series:
# 0 100
# 1 200
# 2 python
# 3 300.12
# 4 400
# dtype: object

# Change the said data type to numeric:
# 0 100.00
# 1 200.00
# 2 NaN
# 3 300.12
# 4 400.00
# dtype: float64

import pandas as pd

ds_orig = pd.Series([100, 200, 'python', 300.12, 400])

print(ds_orig)

ds_out = pd.to_numeric(ds_orig, errors='coerce')

print(ds_out)