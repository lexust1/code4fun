# Write a Pandas program to stack two given series vertically and horizontally.

import pandas as pd

ds1 = pd.Series(['A', 'B', 'C', 'D', 'E'])

ds2 = pd.Series(['Python', 'Rust', 'TensorFlow', 'Java', 'C++'])

res_vert1 = ds1.append(ds2)

res_vert2 = pd.concat([ds1, ds2], axis=0)

res_horz1 = pd.concat([ds1, ds2], axis=1)