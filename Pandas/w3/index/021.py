# Write a Pandas program to drop a index level from a multi-level column 
# index of a dataframe.

import pandas as pd

cols = pd.MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('a', 'z')])
df = pd.DataFrame(data=[[1, 2, 3], [3, 5, 6], [5, 7, 9]],
                  columns=cols)

print(df)

df.columns = df.columns.droplevel(0)
print(df)