# Write a Pandas program to rename all columns with the same pattern of a 
# given DataFrame.

import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
print(df)

print(df.columns)
df.columns = df.columns.str.lower().str.rstrip()
print(df.columns)