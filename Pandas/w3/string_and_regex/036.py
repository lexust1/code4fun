# Write a Pandas program to extract date (format: mm-dd-yyyy) from a given 
# column of a given DataFrame.
import pandas as pd


df = pd.DataFrame(
    {
         'company_code': [
             'Abcd','EFGF', 
             'zefsalf', 
             'sdfslew', 
             'zekfsdf'
         ],
         'date_of_sale': [
             '12/05/2002',
             '16/02/1999',
             '05/09/1998',
             '12/02/2022',
             '15/09/1997'
         ], 
         'sale_amount': [
             12348.5, 
             233331.2, 
             22.5, 
             2566552.0, 
             23.0
        ]
    }
)
print(df)


df["date"] = df["date_of_sale"].str.findall("(0[0-9]|1[0-2])\/(0[0-9]|1[0-9]|2[0-9]|3[0-1])\/(\d\d\d\d)")
print(df)