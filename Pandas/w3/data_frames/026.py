# Write a Pandas program to add one row in an existing DataFrame.

# Sample data:
    
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1

# After add one row:
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1
# 5 10 11 12

import pandas as pd

data1 = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

df1 = pd.DataFrame(data1)

print(df1)


data2 = {'col1': 10, 'col2': 11, 'col3': 12}

df2 = pd.DataFrame(data=data2,
                   index=[0])

print(df2)

df = pd.concat([df1, df2], 
               ignore_index=True)

print(df)


