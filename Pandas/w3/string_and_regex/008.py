# Write a Pandas program to find the index of a substring of DataFrame with 
# beginning and end position.

import pandas as pd

df = pd.DataFrame({
                   'name_code': ['c0001','1000c','b00c2', 'b2c02', 'c2222'],
                   'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998',
                                      '12/02/2022','15/09/1997'],
                   'age': [18.5, 21.2, 22.5, 22, 23]
                   })
print(df)

df['index2'] = df['name_code'].apply(lambda x: x.find('c', 0, 3))
print(df)