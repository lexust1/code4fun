
import pandas as pd
import numpy as np

ds = pd.Series([1, 3, 2, 10, 15, 12, 9, 16, 3])

values = np.diff(np.sign(np.diff(ds)))

res = np.where(values == -2)[0] + 1