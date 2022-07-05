# Write a Pandas program to append data to an empty DataFrame.

import numpy as np
import pandas as pd

df1 = pd.DataFrame()

df2 = pd.DataFrame({'col1': [1, 2, 3], 
                    'col2': [3, 4, 5], 
                    'col3': [7, 8, 9]})

df3 = pd.concat((df1, df2))

print(df1)
print(df2)
print(df3)