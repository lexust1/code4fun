# Write a Pandas program to fill missing values in time series data.

# From Wikipedia , in the mathematical field of numerical analysis, 
# interpolation is a type of estimation, a method of constructing new data 
# points within the range of a discrete set of known data points.

import pandas as pd
import numpy as np
sdata = {"c1":[120, 130 ,140, 150, np.nan, 170], 
         "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}
df = pd.DataFrame(sdata)
print(df)
df.index = pd.util.testing.makeDateIndex()[0:6]
print(df.index)

df.interpolate(inplace=True)
print(df)