# Write a Pandas program to extract only punctuations from the specified 
# column of a given DataFrame.

import pandas as pd

df = pd.DataFrame({
    'company_code': ['c0001.','c000,2','c0003', 'c0003#', 'c0004,'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print(df)

df['punctuation_marks'] = df['company_code'].str.findall("\W")
print(df)