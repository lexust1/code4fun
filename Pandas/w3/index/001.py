# Write a Pandas program to display the default index and set a column as 
# an Index in a given dataframe.

import pandas as pd

df = pd.DataFrame({'school_code': ['s001','s002','s003','s001','s002','s004'],
                   'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                   'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
                            'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                   'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999',
                                     '25/09/1998','11/05/2002','15/09/1997'],
                   'weight': [35, 32, 33, 30, 31, 32],
                   'address': ['street1', 'street2', 'street3', 
                               'street1', 'street2', 'street4'],
                   't_id':['t1', 't2', 't3', 't4', 't5', 't6']})

print(df)

df1 = df.set_index('school_code')
print(df1)

df2 = df.set_index('t_id')
print(df2)