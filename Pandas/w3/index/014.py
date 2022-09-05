# Write a Pandas program to extract a single row, rows and a specific 
# value from a MultiIndex levels DataFrame.

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

print(df.loc['sale1', 'city2'])

print(df.loc['sale1'])

print(df.loc[('sale1', 'city2'), 3])

