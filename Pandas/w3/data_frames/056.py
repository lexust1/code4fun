# Write a Pandas program to get column index from column name of a 
# given DataFrame.

import pandas as pd

data = {'col1': [1, 2, 3, 4,], 
        'col2': [9, 10, 14, 29], 
        'col3': [15, 16, 17, 19]}

df = pd.DataFrame(data)
print(df)

print(df.columns.get_loc('col2'))
