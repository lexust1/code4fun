# 2. Write a Pandas program to convert a Panda module Series to Python list 
# and it’s type.

import pandas as pd

ds = pd.Series([0, 10, 20, 30, 40, 50, 60])
print('1. Data series:\n{}'.format(ds))
print('2. Data series type:\n{}'.format(type(ds)))
print('3. Data series after conversion to list:\n{}'.format(ds.tolist()))
print('4. Data series type after conversion to list:\n{}'.format(type(ds.tolist())))
