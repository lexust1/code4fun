# Write a Pandas program to check whether alpha numeric values present in a 
# given column of a DataFrame.

# Note: isalnum() function returns True if all characters in the string are 
# alphanumeric and there is at least one character, False otherwise.

import pandas as pd

df = pd.DataFrame({
                   'name_code': ['Company','Company a001','Company 123', 
                                 '1234', 'Company 12'],
                   'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998',
                                      '12/02/2022','15/09/1997'],
                   'age': [18.5, 21.2, 22.5, 22, 23]
                   })
print(df)

df['Alphanumeric'] = df['name_code'].str.isalnum()
print(df)