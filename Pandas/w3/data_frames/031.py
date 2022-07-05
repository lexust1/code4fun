# Write a Pandas program to select a row of series/dataframe by given 
# integer index.

# Sample data:
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1

# Index-2: Details
# col1 col2 col3
# 2 3 6 9

import pandas as pd

data = {'col1': [1, 4, 3, 4, 5], 
        'col2': [4, 5, 6, 7, 8], 
        'col3': [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

print(df)

df_new1 = df.iloc[2]
print(df_new1)

df_new2 = df.iloc[[2]]
print(df_new2)

df_new3 = df.iloc[2:3, 0:3]
print(df_new3)

