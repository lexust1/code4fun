# Write a Pandas program to add, subtract, multiple and divide 
# two Pandas Series.

# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])

print('Sum:\n{}'.format(ds1 + ds2))
print('Sub:\n{}'.format(ds1 - ds2))
print('Mult:\n{}'.format(ds1 * ds2))
print('Div:\n{}'.format(ds1 / ds2))