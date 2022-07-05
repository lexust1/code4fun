# Write a Pandas program to create a DataFrame from a Numpy array and 
# specify the index column and column headers.

import numpy as np
import pandas as pd

arr = np.random.rand(12).reshape(3, 4)
print(arr)

df = pd.DataFrame(data=arr,
                  columns=['col1', 'col2', 'col3', 'col4'],
                  index=['row1', 'row2', 'row3'])
print(df)

