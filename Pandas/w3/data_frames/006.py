# Write a Pandas program to select the specified columns and rows from 
# a given DataFrame.

# Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following 
# data frame.

# Sample DataFrame:
    
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
#                       'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 
                         'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=exam_data, index=labels)

print(df)

df1 = df.iloc[[1, 3, 5, 6], [0, 1]]
df2 = df.loc[['b', 'd', 'f', 'g'], ['name', 'score']]

print(df1)
print(df2)