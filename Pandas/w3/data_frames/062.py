# Write a Pandas program to remove first n rows of a given DataFrame.

import pandas as pd

data = {'col1': [1, 2, 3, 4, 5, 6, 7, 15, 20],
        'col2': [10, 15, 3, 4, 6, 7, 8, 9, 1],
        'col3': [10, 25, 2, 2, 7, 9, 8, 7, 3]}

df = pd.DataFrame(data)
print(df)

df_new1 = df.iloc[3:]
print(df_new1)

df.drop([0, 1, 2],
        inplace=True)
print(df)

#del df.iloc[3:]