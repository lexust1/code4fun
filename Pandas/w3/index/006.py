# Write a Pandas program to create a dataframe indexing by date and time.

import pandas as pd

dt_range = pd.date_range(start='2020-05-12 07:10:10', freq='S', periods=10)
print(dt_range)

df_dt = pd.DataFrame(data={'Sales amt': [100, 110, 117, 150, 112, 
                                         99, 129, 135, 140, 150]},
                     index=dt_range)
print(df_dt)