# Write a Pandas program to check whether two given words present in 
# a specified column of a given DataFrame.
import pandas as pd


df = pd.DataFrame(
    {
        'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
        'address': [
            '9910 Surrey Ave.',
            '92 N. Bishop Ave.',
            '9910 Golden Star Ave.', 
            '102 Dunbar St.', 
            '17 West Livingston Court'
        ]
    }
)
print(df)


df["check_two_words"] = df["address"].apply(
    lambda x: ' '.join([el for el in x.split() if "9910" in x and "Ave" in x])
)
print(df)