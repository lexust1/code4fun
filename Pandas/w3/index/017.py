# Write a Pandas program to extract elements in the given positional indices 
# along an axis of a dataframe.

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

print(df.loc[('sale2', 'city2'), 1])

print(df.at[('sale2', 'city2'), 1])

print(df.take([0, 3, 7]))
print(df.take([0, 3, 7], axis=0))
print(df.take([0, 3, 4], axis=1))



