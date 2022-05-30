# Write a Pandas program to convert given series into a dataframe with 
# its index as another column on the dataframe.

import pandas as pd

ds =pd.Series(['A', 'B', 'C', 'D', 'E'])

col1 = ds.index

col2 = ds.values

df = pd.DataFrame({'col1': col1, 'col2': col2})