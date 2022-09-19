# Write a Pandas program to split a string of a column of a given DataFrame 
# into multiple columns.

import pandas as pd

df = pd.DataFrame({'name': ['Alberto  Franco','Gino Ann Mcneill',
                            'Ryan  Parkes', 'Eesha Artur Hinton', 
                            'Syed  Wharton'],
                   'date_of_birth ': ['17/05/2002','16/02/1999',
                                      '25/09/1998','11/05/2002','15/09/1997'],
                   'age': [18.5, 21.2, 22.5, 22, 23]})
print(df)

df[['First Name', 'Middle Name', 'Last Name']] = df['name'].str.split(' ', expand = True)
print(df)