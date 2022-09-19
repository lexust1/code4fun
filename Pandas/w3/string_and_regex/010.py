# Write a Pandas program to check whether alphabetic values present in a given 
# column of a DataFrame.

# Note: isalpha() returns True if all characters in the string are 
# alphabetic and there is at least one character, False otherwise.

import pandas as pd

df = pd.DataFrame({'company_code': ['Company','Company a001','Company 123', 
                                    'abcd', 'Company 12'],
                   'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998',
                                     '12/02/2022','15/09/1997'],
                   'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
print(df)

df['isalpha'] = df['company_code'].str.isalpha()
print(df)
