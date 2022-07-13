# Write a Pandas program to remove infinite values from a given DataFrame.

import numpy as np
import pandas as pd

df = pd.DataFrame([10, 10, 20, 30, np.inf, -np.inf, 38, np.inf])
print(df)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
print(df)