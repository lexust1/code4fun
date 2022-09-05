# Write a Pandas program to remove whitespaces, left sided whitespaces and 
# right sided whitespaces of the string values of a given pandas series.

import pandas as pd

ds = pd.Series([' Green', 'Black ', ' Red ', 'White', ' Pink '])
print(ds)

print(ds.str.strip())
print(ds.str.lstrip())
print(ds.str.rstrip())