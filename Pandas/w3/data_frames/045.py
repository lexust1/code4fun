# Write a Pandas program to find the row for where the value of a given 
# column is maximum.

import numpy as np
import pandas as pd

arr = np.random.rand(75).reshape(25, 3)
print(arr)

df = pd.DataFrame(data=arr,
                  columns=['col1', 'col2', 'col3'])
print(df)

print(df['col2'].argmax())

print(df['col2'].idxmax())
