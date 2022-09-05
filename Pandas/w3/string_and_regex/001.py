# Write a Pandas program to convert all the string values to upper, lower 
# cases in a given pandas series. Also find the length of the string values.

import pandas as pd
import numpy as np

ds = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 
                'CABA', None, 'bird', 'horse', 'dog'])
print(ds)

print(ds.str.upper())
print(ds.str.lower())
print(ds.str.len())