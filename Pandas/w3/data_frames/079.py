# Write a Pandas program to create a DataFrame from the clipboard 
# (data from an Excel spreadsheet or a Google Sheet).

import pandas as pd

df = pd.read_clipboard()

print(df)
    
    

