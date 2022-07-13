# Write a Pandas program to insert a given column at a specific column index 
# in a DataFrame.

import pandas as pd
data = {'col1': [1, 2, 3, 4, 5], 'col2': [3, 6, 8, 9, 11]}

df = pd.DataFrame(data)
print(df)

new_col = [10, 20, 30, 40, 50]

df['col3'] = new_col
print(df)

new_col2 = [10, 30, 69, 90, 100]

df.insert(1, 'col4', new_col2)
print(df)

