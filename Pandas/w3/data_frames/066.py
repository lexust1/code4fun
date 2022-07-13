# Write a Pandas program to select columns by data type of a given DataFrame.

import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print(df)

print(df.select_dtypes(include='number'))
print(df.select_dtypes(include='object'))