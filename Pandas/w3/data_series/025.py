# Write a Pandas program to calculate the number of characters in 
# each word in a given series.

import pandas as pd

ds = pd.Series(['phython', 'solidity', 'golang', 'java', 'django', 'rust'])

def count_ch(word):
    return len(word)
    

res1 = ds.apply(count_ch)

res2 = ds.map(lambda word: len(word))

res3 = ds.apply(len)
