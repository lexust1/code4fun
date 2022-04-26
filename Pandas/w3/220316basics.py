# https://www.w3resource.com/python-exercises/pandas/index.php

import pandas as pd
import numpy as np

# Create dataframe
df = pd.DataFrame({'X':[78,85,96,80,86], 
                   'Y':[84,94,89,83,86], 
                   'Z':[86,97,96,72,83]})

# Create dataseries
ds = pd.Series([2, 4, 6, 8, 10])

# Create test objects
df_test1 = pd.DataFrame(np.random.rand(20, 5))

df_test2 = pd.Series([0, 1, 2, 4, 5])

# Add a date index
df.index = pd.date_range('1900/1/30', periods=df.shape[0])

# View/inspecting data

df.head(3)

df.tail(2)

df.shape

df.info()

df.describe()

df.value_counts(dropna=False)

df.apply(pd.Series.value_counts)

# Selection 

ds_test1 = df['Y']

df_test3 = df[['X', 'Z']]

df.iloc[0]

df.loc['1900-02-01']

df.iloc[0, :]

df.iloc[2, 2]

# Data Cleaning

