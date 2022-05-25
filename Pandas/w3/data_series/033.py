# Write a Pandas program to replace missing white spaces in a given string 
# with the least frequent character.

import pandas as pd

str = 'abc def abcdef icd'

ds = pd.Series(list(str))

freq_val = ds.value_counts()

print(freq_val)

least_freq = freq_val.index[-1]

res = "".join(ds.replace(' ', least_freq)) 
