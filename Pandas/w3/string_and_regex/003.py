# Write a Pandas program to add leading zeros to the integer column in a pandas
# series and makes the length of the field to 8 digit.

import pandas as pd

# 1
df = pd.DataFrame({'amount': [10, 250, 3000, 40000, 500000]})
print(df)

def leading_zeros(num):
    return '{:0>8}'.format(num)

df['amount'] = df['amount'].apply(leading_zeros)
print(df)

# 2
df1 = pd.DataFrame({'amount': [10, 250, 3000, 40000, 500000]})
print(df1)

df1['amount'] = df1['amount'].apply(lambda num: '{:0>8}'.format(num))
print(df1)

# 3
df2 = pd.DataFrame({'amount': [10, 250, 3000, 40000, 500000]})
print(df2)

def leading_zeros2(num):
    return str(num).zfill(8)

df2['amount'] = df2['amount'].apply(leading_zeros2)
print(df2)

# 4

df3 = pd.DataFrame({'amount': [10, 250, 3000, 40000, 500000]})
print(df3)

df3['amount'] = df3['amount'].apply(lambda num: str(num).zfill(8))
print(df3)
    


