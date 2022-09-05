# Write a Pandas program to rename names of columns and specific labels of 
# the Main Index of the MultiIndex dataframe.

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

df.rename(columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'}, 
          inplace=True)
print(df)

df.rename(index={'sale2': 'S2', 'city2': 'C2'},
          inplace=True)
print(df)