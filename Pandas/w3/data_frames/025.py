# Write a Pandas program to change the order of a DataFrame columns.

# Sample data:
    
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1

# After altering col1 and col3
# col3 col2 col1
# 0 7 4 1
# 1 8 5 4
# 2 9 6 3
# 3 0 7 4
# 4 1 8 5

import pandas as pd

data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

print(df)

print(df[['col3', 'col2', 'col1']])