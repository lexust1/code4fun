# Write a Pandas program to extract year between 1800 to 2200 from 
# the specified column of a given DataFrame.

import pandas as pd

df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print(df)

df["year digit"] = df["year"].str.findall("[\d]{4}").str[0].astype(int) 
print(df)

df["year digit"] = df["year digit"].where((df["year digit"] >= 1800) & 
                                          (df["year digit"] <= 2200))
print(df)

