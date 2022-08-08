# Write a Pandas program to convert continuous values of a column in 
# a given DataFrame to categorical.
# { 'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'], 'Age': [18, 22, 40, 50, 80, 5] }
# Output:
# Age group:
# 0 kids
# 1 adult
# 2 elderly
# 3 adult
# 4 elderly
# 5 kids
# Name: age_groups, dtype: category
# Categories (3, object): [kids < adult < elderly]



import pandas as pd
df = pd.DataFrame({'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
                            'Eesha Hinton', 'Syed Wharton', 'Tony Bale'],
                   'Age': [18, 22, 40, 50, 80, 5]})
print(df)

df['Age groups'] = pd.cut(x=df['Age'],
                          bins=[0, 18, 65, 99],
                          labels=['kid', 'adult', 'elderly'])

print(df)