# Write a Pandas program to split a given DataFrame into two random subsets.

import pandas as pd

df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': ['18', '21', '22', '22', '23']
})
print(df)

df1 = df.sample(frac=0.6)
df2 = df.drop(df1.index)
print(df1)
print(df2)
