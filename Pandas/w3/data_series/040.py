# Write a Pandas program to check inequality over the index axis of a given 
# dataframe and a given series.

import pandas as pd

df = pd.DataFrame({'W':[68,75,86,80,None],
                        'X':[78,75,None,80,86], 
                        'Y':[84,94,89,86,86],
                        'Z':[86,97,96,72,83]});
ds = pd.Series([68, 75, 86, 80, None]) 

print(df.ne(ds, axis=0))