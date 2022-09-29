# Write a Pandas program to extract only non alphanumeric characters 
# from the specified column of a given DataFrame.

import pandas as pd

df = pd.DataFrame({
                    'company_code': ['c0001#','c00@0^2','$c0003', 
                                     'c0003', '&c0004'],
                    'year': ['year 1800','year 1700','year 2300', 
                             'year 1900', 'year 2200']
                    })
print(df)

df["nonalphanum"] = df['company_code'].str.findall("\W")
print(df)