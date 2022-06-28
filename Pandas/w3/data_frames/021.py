# Write a Pandas program to iterate over rows in a DataFrame.

# Sample Python dictionary data and list labels:
# exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, 
#              {'name':'Katherine','score':16.5}]


import pandas as pd

exam_data = ([{'name':'Anastasia', 'score':12.5}, 
              {'name':'Dima','score':9}, 
              {'name':'Katherine','score':16.5}])

df = pd.DataFrame(exam_data)

print(df)

for idx, row in df.iterrows():
    print(idx, row['name'], row['score'])
    
[print(idx, row['name'], row['score']) for idx, row in df.iterrows()]    