# Write a Pandas program to drop a list of rows from a specified DataFrame.

# Sample data:
    
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1

# New DataFrame after removing 2nd & 4th rows:
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 3 4 7 0

import pandas as pd

data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

print(df)

df.drop([2, 4], inplace=True)

print(df)