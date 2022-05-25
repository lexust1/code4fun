# Write a Pandas program to filter words from a given series that contain 
# at least two vowels.

import pandas as pd

ds = pd.Series(['Python', 'Java', 'Rust', 'TensorFlow', 'Pandas'])

def vowels(word):
    count = 0
    for ch in word:
        if ch.lower() in 'aeiou':
            count += 1
    if count >= 2:
        return True
    else: 
        return False

res1 = ds[ds.apply(vowels)]