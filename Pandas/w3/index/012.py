# Write a Pandas program to construct a series using the MultiIndex levels 
# as the column and index.

import pandas as pd
import numpy as np

sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 
                 'sale3', 'sale3', 'sale4', 'sale4'],
                ['city1', 'city2', 'city1', 'city2', 
                 'city1', 'city2', 'city1', 'city2']]

sales_tuples = list(zip(*sales_arrays))

sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print(sales_tuples)

s = pd.Series(np.random.randn(8), index = sales_index)
print(s)
