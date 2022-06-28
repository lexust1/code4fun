# Write a Pandas program to rename columns of a given DataFrame.

# Sample data:
    
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 2 5 8
# 2 3 6 9

# New DataFrame after renaming columns:
# Column1 Column2 Column3
# 0 1 4 7
# 1 2 5 8
# 2 3 6 9

import pandas as pd

data = {'col1': [1, 2, 3],
        'col2': [4, 5, 6],
        'col3': [7, 8, 9]}

df = pd.DataFrame(data=data)

print(df)

cols = ['Column1', 'Column2', 'Column3']

df.columns = cols

print(df)

