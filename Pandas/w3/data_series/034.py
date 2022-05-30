# Write a Pandas program to compute the autocorrelations of a given 
# numeric series.

# From Wikipedia:
# Autocorrelation, also known as serial correlation, is the correlation 
# of a signal with a delayed copy of itself as a function of delay. 
# Informally, it is the similarity between observations as a function of 
# the time lag between them.

import pandas as pd
import numpy as np

ds = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))

res = ds.autocorr()

res2 = [ds.autocorr(idx) for idx in range(14)]