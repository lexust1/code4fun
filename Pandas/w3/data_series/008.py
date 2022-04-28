# Write a Pandas program to convert the first column of a DataFrame 
# as a Series.
import pandas as pd

d = {'col1': [0, 1, 2, 3, 4, 5], 
      'col2': [1, 2, 3, 4, 5, 6], 
      'col3': [10, 20, 30, 40, 50, 60]}

df = pd.DataFrame(d)

ds1 = df['col1']
ds2 = df.iloc[:, 0]
ds3 = df[df.columns[0]]

print(d, '\n')
print(df, '\n')
print(ds1, '\n')
print(ds2, '\n')
print(ds3, '\n')