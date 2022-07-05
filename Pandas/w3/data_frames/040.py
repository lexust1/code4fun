# Write a Pandas program to shuffle a given DataFrame rows.

# Sample data:

# Original DataFrame:
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

# New DataFrame:
# attempts name qualify score
# 5 3 Michael yes 20.0
# 0 1 Anastasia yes 12.5
# 9 1 Jonas yes 19.0
# 6 1 Matthew yes 14.5
# 7 1 Laura no NaN
# 1 3 Dima no 9.0
# 3 3 James no NaN
# 4 2 Emily no 9.0
# 8 2 Kevin no 8.0
# 2 2 Katherine yes 16.5

import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                         'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

print(df)

df = df.sample(frac=1)

print(df)