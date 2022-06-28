# Write a Pandas program to count city wise number of people from a given of 
# data set (city, name of the person).

# Sample data:
# city Number of people
# 0 California 4
# 1 Georgia 2
# 2 Los Angeles 4

# {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 
#           'Emily', 'Michael', 'Matthew', 'Laura', 
#           'Kevin', 'Jonas'],
# 'city': ['California', 'Los Angeles', 'California', 'California', 
#          'California', 'Los Angeles', 'Los Angeles', 'Georgia', 
#          'Georgia', 'Los Angeles']}

import pandas as pd

data =  {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 
                  'Emily', 'Michael', 'Matthew', 'Laura', 
                  'Kevin', 'Jonas'],
         'city': ['California', 'Los Angeles', 'California', 'California', 
                  'California', 'Los Angeles', 'Los Angeles', 'Georgia', 
                  'Georgia', 'Los Angeles']}

df = pd.DataFrame(data)

print(df)

df_count = df.groupby('city').count()
df_count.rename(columns={'name':'Num of people'}, inplace=True)

print(df_count)

