# Write a Pandas program to create DataFrames that contains random values, 
# contains missing values, contains datetime values and contains mixed values.

import pandas as pd

df1 = pd.util.testing.makeDataFrame() 
print(df1)

df2 = pd.util.testing.makeMissingDataframe() 
print(df2)

df3 = pd.util.testing.makeTimeDataFrame()
print(df3)

df4 = pd.util.testing.makeMixedDataFrame()
print(df4)