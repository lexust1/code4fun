# Write a Pandas program to sort a MultiIndex of a DataFrame.
#  Also sort on various levels of index.

import pandas as pd
import numpy as np

sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 
                 'sale3', 'sale3', 'sale4', 'sale4'],
                ['city1', 'city2', 'city1', 'city2', 
                 'city1', 'city2', 'city1', 'city2']]

sales_tuples = list(zip(*sales_arrays))

sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print(sales_tuples)

df = pd.DataFrame(np.random.randn(8, 5), index=sales_index)
print(df)

df1 = df.sort_index()
print(df1)

df2 = df.sort_index(level=0)
print(df2)

df3 = df.sort_index(level=1)
print(df3)

df4= df.sort_index(level='city')
print(df4)
