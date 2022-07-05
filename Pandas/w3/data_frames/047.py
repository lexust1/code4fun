# Write a Pandas program to get the specified row value of a given DataFrame.

import pandas as pd

data = {'col1': [1, 2, 4, 7], 'col2': [1, 3, 9, 10], 'col3': [1, 10, 14, 21]}

df = pd.DataFrame(data)

print(df)

print(df.iloc[3])