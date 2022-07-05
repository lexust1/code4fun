# Write a Pandas program to convert index in a column of the given dataframe.

# Sample data:
# Original DataFrame
# attempts name qualify score
# 0 1 Anastasia yes 12.5
# 1 3 Dima no 9.0
# 2 2 Katherine yes 16.5
# 3 3 James no NaN
# 4 2 Emily no 9.0
# 5 3 Michael yes 20.0
# 6 1 Matthew yes 14.5
# 7 1 Laura no NaN
# 8 2 Kevin no 8.0
# 9 1 Jonas yes 19.0

# After converting index in a column:
# index attempts name qualify score
# 0 0 1 Anastasia yes 12.5
# 1 1 3 Dima no 9.0
# 2 2 2 Katherine yes 16.5
# 3 3 3 James no NaN
# 4 4 2 Emily no 9.0
# 5 5 3 Michael yes 20.0
# 6 6 1 Matthew yes 14.5
# 7 7 1 Laura no NaN
# 8 8 2 Kevin no 8.0
# 9 9 1 Jonas yes 19.0

# Hiding index:
# index attempts name qualify score
# 0 1 Anastasia yes 12.5
# 1 3 Dima no 9.0
# 2 2 Katherine yes 16.5
# 3 3 James no NaN
# 4 2 Emily no 9.0
# 5 3 Michael yes 20.0
# 6 1 Matthew yes 14.5
# 7 1 Laura no NaN
# 8 2 Kevin no 8.0
# 9 1 Jonas yes 19.0

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                         'yes', 'yes', 'no', 'no', 'yes']}

df = pd.DataFrame(exam_data)

print(df)

df.reset_index(inplace=True)

print(df)

df.drop('index', axis=1, inplace=True)

print(df)

