# Write a Pandas program to check whether a given column is present in a 
# DataFrame or not.

import numpy as np
import pandas as pd

data = {'col1': [1, 2, 4, 7], 'col2': [1, 3, 9, 10], 'col3': [1, 10, 14, 21]}

df = pd.DataFrame(data)

print(df)

print(True) if 'col2' in df.columns else print(False)

    