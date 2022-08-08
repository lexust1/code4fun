# Write a Pandas program to display memory usage of a given DataFrame and 
# every column of the DataFrame.

import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})

print('\n\ndf:\n', df)

print('\n\ndf.info:\n', df.info())

print('\n\ndf.info(memory_usage=deep):\n', df.info(memory_usage='deep'))

print('\n\ndf.memory_usage(deep = True):\n', df.memory_usage(deep=True))