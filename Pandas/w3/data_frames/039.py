# Write a Pandas program to combining two series into a DataFrame.

# Sample data:
# Data Series:
# 0 100
# 1 200
# 2 python
# 3 300.12
# 4 400
# dtype: object

# 0 10
# 1 20
# 2 php
# 3 30.12
# 4 40
# dtype: object

# New DataFrame combining two series:
# 0 1
# 0 100 10
# 1 200 20
# 2 python php
# 3 300.12 30.12
# 4 400 40

import pandas as pd

ds1 = pd.Series([100, 200, 'python', 300.12, 400])

ds2 = pd.Series([10, 20, 'php', 30.12, 40])

print(ds1)
print(ds2)

df = pd.concat([ds1, ds2], axis=1)

print(df)

