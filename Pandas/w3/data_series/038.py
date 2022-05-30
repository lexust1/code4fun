 # Write a Pandas program to check the equality of two given series.
import pandas as pd

ds1 = pd.Series([0, 1, 2, 5, 8, 9, 13, 21, 15])
ds2 = pd.Series([0, 1, 2, 5, 13, 22, 17, 21, 15])

print(ds1 == ds2)
