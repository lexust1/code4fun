# Write a Pandas program to widen output display to see more columns.

# Sample data:
    
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 4 5 8
# 2 3 6 9
# 3 4 7 0
# 4 5 8 1

import pandas as pd

data = {'col1': [1, 4, 3, 4, 5],
        'col2': [4, 5, 6, 7, 8],
        'col3': [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

print(df)

pd.set_option('display.max_columns', 500)