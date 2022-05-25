# Compute difference of differences between consecutive 
# numbers of a given series

import numpy as np
import pandas as pd

ds = pd.Series([1, 3, 4, 29, 87, 96, 127])

res = ds.diff()

res_lst = res.tolist()