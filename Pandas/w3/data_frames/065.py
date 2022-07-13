# Write a Pandas program to reverse order (rows, columns) of a given DataFrame.

import pandas as pd

df = pd.DataFrame({'W':[68,75,86,80,66],
                   'X':[78,85,96,80,86], 
                   'Y':[84,94,89,83,86],
                   'Z':[86,97,96,72,83]})
print(df)

# Reverse rows
df1 = df.iloc[::-1, :]
print(df1)

# Reverse columns
df2 = df.iloc[:, ::-1]
print(df2)

# Reverse rows and columns
df3 = df.iloc[::-1, ::-1]
print(df3)