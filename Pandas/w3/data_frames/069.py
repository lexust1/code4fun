# Write a Pandas program to merge datasets and check uniqueness.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 
             'Syed Wharton', 'John Lee', 'Tony Smith', 'Kira Mattews'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002',
                       '15/09/1997', '15/09/1987', '15/09/1977', '15/09/1967' ],
    'Age': [18.5, 21.2, 22.5, 22, 23, 33, 43, 53]
})
print('df:\n', df)

df1 = df.copy(deep=True)
df2 = df.copy(deep=True)

df1 = df1.sample(frac=0.8)
df2 = df2.sample(frac=0.4)

print('df1:\n', df1)
print('df2:\n', df2)

df3 = pd.merge(df1, df2, validate="one_to_one")
print('df3:\none_to_one:\n', df3)

df4 = pd.merge(df1, df2, validate="one_to_many")
print('df4:\none_to_many:\n', df4)

df5 = pd.merge(df1, df2, validate="many_to_one")
print('df5:\nmany_to_one:\n', df5)