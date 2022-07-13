# Write a Pandas program to group by the first column and get second 
# column as lists in rows.

import pandas as pd
df = pd.DataFrame({'col1':['C1','C1','C2','C2','C2','C3','C2'], 
                   'col2':[1,2,3,3,4,6,5]})
print(df)


print(df.groupby('col1')['col2'].apply(list))