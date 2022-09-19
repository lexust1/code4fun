# Write a Pandas program to check if a specified column starts with a 
# specified string in a DataFrame.

import pandas as pd

df = pd.DataFrame({'company_code': ['Abcd','EFGF', 'zefsalf', 
                                    'sdfslew', 'zekfsdf'],
                   'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998',
                                    '12/02/2022','15/09/1997'],
                   'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
print(df)

df['startswith'] = df['company_code'].str.startswith('ze')
print(df)