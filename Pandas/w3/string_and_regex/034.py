# Write a Pandas program to extract numbers less than 100 from the specified 
# column of a given DataFrame.
import pandas as pd


df = pd.DataFrame(
    {
        'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'], 
        'address': [
            '72 Surrey Ave.11',
            '92 N. Bishop Ave.',
            '9910 Golden Star St.', 
            '102 Dunbar St.', 
            '17 West Livingston Court'
        ]
    }
)
print(df)


df["<100"] = (
    df["address"].str.findall("(\d+)")
    .apply(lambda x: [el for el in x if int(el) < 100])
)
print(df)