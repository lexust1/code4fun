# Write a Pandas program to sort a given DataFrame by two or more columns.


import pandas as pd



df = pd.DataFrame({'col1': [1, 2, 3, 1, 5, 15, 3, 10], 
                   'col2': [3, 4, 5, 1, 25, 15, 37, 10], 
                   'col3': [7, 8, 9, 1, 51, 15, 30, 10]})
print(df)

df.sort_values(by=['col2', 'col3'], 
               ascending=False, 
               inplace=True)

print(df)