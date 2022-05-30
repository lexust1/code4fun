# Write a Pandas program to get the powers of an array values element-wise.
# Note: First array elements raised to powers from second array
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

import pandas as pd

df = pd.DataFrame({'X': [78, 85, 96, 80, 86], 
                   'Y': [84, 94, 89, 83, 86],
                   'Z': [86, 97, 96, 72, 83]})

df_pow = pd.DataFrame({'X': [0, 1, 2, 3, 1],
                       'Y': [2, 4, 5, 7, 0],
                       'Z': [1, 2, 3, 2, 1]})

df.pow(df_pow)