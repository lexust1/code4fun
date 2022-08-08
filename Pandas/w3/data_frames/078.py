# Write a Pandas program to replace the current value in a dataframe column 
# based on last largest value. 

# If the current value is less than last largest value replaces the value 
# with 0.

import pandas as pd

data = {'rnum': [23, 21, 27, 22, 34, 33, 34, 31, 25, 22, 34, 19, 31, 32, 19]}
df = pd.DataFrame(data)
print(df)

df.where(df == df.cummax(), 0, inplace=True)
print(df)