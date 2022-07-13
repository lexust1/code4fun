# Write a Pandas program to add a prefix or suffix to all columns of 
# a given DataFrame.

import pandas as pd

df = pd.DataFrame({'W':[68,75,86,80,66],
                   'X':[78,85,96,80,86], 
                   'Y':[84,94,89,83,86],
                   'Z':[86,97,96,72,83]})
print(df)

df1 = df.add_prefix('A_')
print(df1)

df2 = df.add_suffix('_1')
print(df2)
