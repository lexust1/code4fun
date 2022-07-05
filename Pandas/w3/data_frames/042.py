# Write a Pandas program to rename a specific column name in a given DataFrame.

# Sample data:
    
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 2 5 8
# 2 3 6 9

# New DataFrame after renaming second column:
# col1 Column2 col3
# 0 1 4 7
# 1 2 5 8
# 2 3 6 9

import pandas as pd

data = {'col1': [1, 2, 3,], 
        'col2': [4, 5, 6], 
        'col3': [7, 8, 9]}

df = pd.DataFrame(data)

print(df)

df.rename(columns={'col2': 'Column2'}, 
          inplace=True)

print(df)