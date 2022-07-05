# Write a Pandas program to get a list of a specified column of a DataFrame.

# Sample data:
# Powered by
# Original DataFrame

# col1 col2 col3
# 0 1 4 7
# 1 2 5 8
# 2 3 6 9

# Col2 of the DataFrame to list:
# [4, 5, 6]

import pandas as pd

data = {'col1': [1, 2, 3], 
        'col2': [4, 5, 6],
        'col3': [7, 8, 9]}

df = pd.DataFrame(data)

print(df)


print(df['col2'].tolist())


