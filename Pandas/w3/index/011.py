# Write a Pandas program to check if a specified value exists in single 
# and multiple column index dataframe.
# Write a Pandas program to convert index of a given dataframe into a column.

import pandas as pd

df = pd.DataFrame(data={'school_code': ['s001','s002','s003',
                                        's001','s002','s004'],
                        'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                        'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes',
                                 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                        'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999',
                                          '25/09/1998','11/05/2002','15/09/1997'],
                        'weight': [35, 32, 33, 30, 31, 32],
                        'address': ['street1', 'street2', 'street3', 
                                    'street1', 'street2', 'street4']}, 
                  index=['t1', 't2', 't3', 't4', 't5', 't6'])

print(df)

print('t1' in df.index)
print('t11' in df.index)



df2 = pd.DataFrame(data={'school_code': ['s001','s002','s003',
                                        's001','s002','s004'],
                        'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                        'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes',
                                 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                        'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999',
                                          '25/09/1998','11/05/2002','15/09/1997'],
                        'weight': [35, 32, 33, 30, 31, 32],
                        'address': ['street1', 'street2', 'street3', 
                                    'street1', 'street2', 'street4'], 
                        't_id': ['t1', 't2', 't3', 't4', 't5', 't6']
                        })

print(df2)

df2.set_index(['t_id', 'school_code', 'class'], inplace=True)
print(df2)

print('t3' in df2.index.levels[0])
print('t3' in df2.index.levels[1])
print('t3' in df2.index.levels[2])