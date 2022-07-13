# Write a Pandas program to get last n records of a DataFrame.


import pandas as pd

data = {'col1': [1, 2, 3, 4, 10, 19, 13], 
        'col2': [9, 10, 14, 29, 10, 15, 20], 
        'col3': [15, 16, 17, 19, 20, 30, 50]}

df = pd.DataFrame(data)
print(df)

print(df.tail(3))

print(df.iloc[-3:, :])

