# Write a Pandas program to create an index labels by using 64-bit integers, 
# using floating-point numbers in a given dataframe.

import pandas as pd

df_int64 = pd.DataFrame(data=
                  {'school_code': ['s001','s002','s003','s001','s002','s004'],
                   'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                   'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
                            'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                   'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999',
                                     '25/09/1998','11/05/2002','15/09/1997'],
                   'weight': [35, 32, 33, 30, 31, 32],
                   'address': ['street1', 'street2', 'street3', 
                               'street1', 'street2', 'street4'],
                   't_id':['t1', 't2', 't3', 't4', 't5', 't6']},
                  index=list(range(1, 7)))
print(df_int64)


df_float64 = pd.DataFrame(data=
                  {'school_code': ['s001','s002','s003','s001','s002','s004'],
                   'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                   'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
                            'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
                   'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999',
                                     '25/09/1998','11/05/2002','15/09/1997'],
                   'weight': [35, 32, 33, 30, 31, 32],
                   'address': ['street1', 'street2', 'street3', 
                               'street1', 'street2', 'street4'],
                   't_id':['t1', 't2', 't3', 't4', 't5', 't6']},
                  index=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
print(df_float64)


                           
                           