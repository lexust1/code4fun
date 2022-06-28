# Write a Pandas program to append a new row 'k' to DataFrame with given 
# values for each column. Now delete the new row and return the original 
# data frame.

# Sample DataFrame:
    
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
#                       'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Values for each column will be:
# name : ‘Suresh’, score: 15.5, attempts: 1, qualify: ‘yes’, label: ‘k’

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 
                         'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=exam_data,
                  index=labels)

print(df)

df.loc['k'] = ['Suresh', 15.5, 1, 'yes']

print(df) 

df.drop('k', inplace=True)

print(df)