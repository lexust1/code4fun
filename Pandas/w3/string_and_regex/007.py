# Write a Pandas program to find the index of a given substring of 
# a DataFrame column.

import pandas as pd

df = pd.DataFrame({'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
                   'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998',
                                      '12/02/2022','15/09/1997'],
                   'age': [18.5, 21.2, 22.5, 22, 23]})
print(df)

def string_index(string):
    return string.find('22')

df['index1'] = df['name_code'].apply(string_index)
print(df)

df['index2'] = df['name_code'].apply(lambda x: x.find('22'))
print(df)