# Write a Pandas program convert the first and last character of each word 
# to upper case in each word of a given series.

import pandas as pd

ds = pd.Series(['python', 'solidity', 'go', 'java', 'rust'])

# res = ds.map('{}'.format)


# def ch_lets():
#     return [word[0].upper()+word[1:-1]+word[-1].upper() for word in ds]
    

# 1
def ch_lets(word):
    return word[0].upper()+word[1:-1]+word[-1].upper()

res = ds.apply(ch_lets)

# 2
res1 = ds.map(lambda word: word[0].upper()+word[1:-1]+word[-1].upper())