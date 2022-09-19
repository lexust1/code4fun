# Write a Pandas program to extract email from a specified column of string 
# type of a given DataFrame.

import pandas as pd
import re

#pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'name_email': ['Alberto Franco af@gmail.com','Gino Mcneill gm@yahoo.com',
                   'Ryan Parkes rp@abc.io', 'Eesha Hinton', 
                   'Gino Mcneill gm@github.com']
    })
print(df)

df['email'] = df['name_email'].str.findall('\S+@\S+')
print(df)

def extract_email(text):
    email = re.findall('\S+@\S+', text)
    return email
    
df['email2'] = df['name_email'].apply(extract_email)
print(df)
    
df['email3'] = df['name_email'].apply(lambda text: re.findall('\S+@\S+', text))
print(df)