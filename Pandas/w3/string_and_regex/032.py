# Write a Pandas program to remove repetitive characters from the specified 
# column of a given DataFrame.

import pandas as pd


df = pd.DataFrame(
    {
        'text_code': ['t0001.', 't0002', 't0003', 't0004'], 
        'text_lang': [
            'She livedd a long life.', 
            'How oold is your father?', 
            'What is tthe problem?', 
            'TThhis desk is used by Tom.'
        ]
    }
)
print(df)

df["rep char"] = df["text_lang"].str.findall(r"(\w)\1+")
print(df)
