# Write a Pandas program to extract numbers greater than 940 from the 
# specified column of a given DataFrame.
import pandas as pd
from typing import List 


df = pd.DataFrame(
    {
        'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'], 
        'address': [
            '7277 Surrey Ave.1111',
            '920 N. Bishop Ave.',
            '9910 Golden Star St.', 
            '1025 Dunbar St.', 
            '1700 West Livingston Court'
        ]
    }
)
print(df)


def compare_values(list_of_values: List[str]) -> List[int]:
    output_list = [el for el in list_of_values if int(el) > 940]
    return output_list
print(compare_values([0, 10, 900, 940, 1000, 10000]))


# df[">940"] = (
#     df["address"].str.findall("(\d+)")
#     .apply(compare_values)
# )
# print(df)


df[">940"] = (
    df["address"].str.findall("(\d+)")
    .apply(lambda x:  [el for el in x if int(el) > 940])
)
print(df)

