# Write a Pandas program to convert DataFrame column type from string to 
# datetime.

# Sample data:
# String Date:
# 0 3/11/2000
# 1 3/12/2000
# 2 3/13/2000
# dtype: object

# Original DataFrame (string to datetime):
# 0
# 0 2000-03-11
# 1 2000-03-12
# 2 2000-03-13

import pandas as pd

ds1 = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])

print(ds1)

ds1_new = pd.to_datetime(ds1)

print(ds1_new)

df = pd.DataFrame(ds1_new)

print(df)