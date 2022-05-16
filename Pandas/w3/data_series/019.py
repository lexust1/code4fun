# Write a Pandas program to calculate the frequency counts of each 
# unique value of a given series.
import numpy as np
import pandas as pd

arr_cont = np.random.RandomState(10)
arr = arr_cont.randint(0, 10, 100)

fr_val = pd.Series(arr).value_counts()