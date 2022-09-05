# Write a Pandas program to add leading zeros to the character column in 
# a pandas series and makes the length of the field to 8 digit.

import pandas as pd

df = pd.DataFrame({'amount': [10, 250, 3000, 40000, 500000]})
print(df)

df['amount']=df['amount'].apply(lambda num: str(num).zfill(8))
print(df)
