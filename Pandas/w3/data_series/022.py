# Write a Pandas program to extract items at given positions 
# of a given series.

import pandas as pd

ds = pd.Series(list('2390238923902390239023'))

ext_els = ds.iloc[[0, 2, 10, 15]]


