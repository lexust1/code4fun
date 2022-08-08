# Write a Pandas program to combine many given series to create a DataFrame.

import pandas as pd

ds1 = pd.Series(['python', 'C', 'Rust', 'Go', 'Java', 'SQL'])
ds2 = pd.Series([1, 2, 3, 4, 5, 6])
ds3 = pd.Series([0.1, 0.7, 0.5, 1.3, 3.8, 10.0])

print(ds1)
print(ds2)
print(ds3)

df = pd.concat([ds1, ds2, ds3], 
               axis=1)
print(df)