# Write a Pandas program to find integer index of rows with missing data 
# in a given dataframe.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
             'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999',
                      '25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, None, 33, 30, 31, None]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])

print(df)
index = df['weight'].index[df['weight'].apply(np.isnan)]
df_index = df.index.values.tolist()
print(df_index)
print([df_index.index(i) for i in index])