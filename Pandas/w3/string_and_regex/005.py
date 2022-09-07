# Write a Pandas program to capitalize all the string values of specified 
# columns of a given DataFrame.

import pandas as pd

df = pd.DataFrame({'name': ['alberto','gino','ryan', 'Eesha', 'syed'],
                   'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998',
                                      '11/05/2002','15/09/1997'],
                   'age': [18.5, 21.2, 22.5, 22, 23]})
print(df)

df['name'] = df['name'].str.capitalize()
print(df)