# Write a Pandas program to extract hash attached word from twitter text 
# from the specified column of a given DataFrame.

import pandas as pd
import re

df = pd.DataFrame({'tweets': ['#Obama says goodbye',
                              'Retweets for #cash',
                              'A political endorsement in #Indonesia', 
                              '1 dog = many #retweets', 
                              'Just a simple #egg']})
print(df)

df['cash1'] = df['tweets'].str.findall('(?<=#)\S+').str[0]

print(df)