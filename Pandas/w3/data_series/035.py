# Write a Pandas program to create a TimeSeries to display all the Sundays 
# of given year.

import pandas as pd

res = pd.date_range(start='2021-01-01', periods=52, freq='W-SUN')
print(res)

res2 = pd.date_range(start='2021-01-01', end='2021-12-31', freq='W-SUN')
print(res2)

res3 = pd.date_range(start='2021-01-01', end='2021-12-31', freq='W-FRI')
print(res3)