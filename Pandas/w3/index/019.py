# Write a Pandas program to select a specific row of given series/dataframe 
# by integer index.

import pandas as pd

ds = pd.Series([1, 3, 5, 7, 9, 11, 13, 15], index=range(0, 8))
print(ds)

print(ds.iloc[6])

df = pd.DataFrame({'school_code': ['s001','s002','s003','s001','s002','s004'],
                   'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                   'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
                            'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                   'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999',
                                     '25/09/1998','11/05/2002','15/09/1997'],
                   'weight': [35, 32, 33, 30, 31, 32]
    })
print(df)
print(df.iloc[3])