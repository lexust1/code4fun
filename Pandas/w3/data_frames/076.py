# Write a Pandas program to clean object column with mixed data of a given 
# DataFrame using regular expression.

import pandas as pd


data = {"agent": ["a001", "a002", "a003", "a003", "a004"], 
        "purchase":[4500.00, 7500.00, "$3000.25", "$1250.35", "9000.00"]}

df = pd.DataFrame(data)
print(df)

df['purchase'].replace("[$,]", "", regex=True).astype(float)