# Write a Pandas program to insert a column at a specific index 
# in a given DataFrame.

import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 
             'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  [1, 2, 3, 4, 5, 6])
print(df)

date_of_birth = ['15/05/2002','17/05/2002','16/02/1999',
                 '25/09/1998','11/05/2002','15/09/1997'] 

df.insert(loc=3, 
          column='date_of_birth',
          value=date_of_birth);

print(df)