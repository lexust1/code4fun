# Write a Pandas program to convert a given list of lists into a Dataframe.

import pandas as pd
list_of_lists = [['col1', 'col2'], [2, 4], [1, 3]]

cols = list_of_lists.pop(0)
print(cols)
print(list_of_lists)

df = pd.DataFrame(data=list_of_lists,
                  columns=cols)
print(df)