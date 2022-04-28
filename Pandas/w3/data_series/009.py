# Write a Pandas program to convert a given Series to an array.

import pandas as pd
import numpy as np

ds = pd.Series([10, 20, 30, 40, 50, 60])

arr = ds.values

arr1 = np.array(ds)

arr2 = np.array(ds.values)

arr3 = np.array(ds.values.tolist())

arr4 = ds.to_numpy()

print(ds)
print(arr)
print(type(arr))
print(arr1)
print(type(arr1))
print(arr2)
print(type(arr2))
print(arr3)
print(type(arr3))
print(arr4)
print(type(arr4))