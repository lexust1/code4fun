# Write a Pandas program to write a DataFrame to CSV file using tab separator.

# Sample data:
    
# Original DataFrame

# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1

# Data from new_file.csv file:
# col1\tcol2\tcol3
# 0 1\t4\t7
# 1 4\t5\t8
# 2 3\t6\t9
# 3 4\t7\t0
# 4 5\t8\t1

import pandas as pd

data = {'col1': [1, 4, 3, 4, 5], 
        'col2': [4, 5, 6, 7, 8], 
        'col3': [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

print(df)

df.to_csv('new_file.csv', sep='\t', index=False)

df_new = pd.read_csv('new_file.csv')

print(df_new)