# Write a Pandas program to extract word mention someone in tweets using @ 
# from the specified column of a given DataFrame.

import pandas as pd

df = pd.DataFrame({'tweets': ['@Obama says goodbye',
                              'Retweets for @cash',
                              'A political endorsement in @Indonesia', 
                              '1 dog = many #retweets', 
                              'Just a simple #egg']})
print(df)

#df['@'] = df['tweets'].str.findall('(?<=#)\S+').str[0]

df['@'] = df['tweets'].str.findall("(?<=@)\S+").str[0]
print(df)