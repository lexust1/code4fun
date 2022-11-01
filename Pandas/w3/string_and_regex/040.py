# Write a Pandas program to extract words starting with capital words from 
# a given column of a given DataFrame.
import pandas as pd


def main():
    df = pd.DataFrame(
        {
            'company_code': [
                'Abcd',
                'EFGF', 
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
            'address': [
                '9910 Surrey Avenue',
                '92 N. Bishop Avenue',
                '9910 Golden Star Avenue', 
                '102 Dunbar St.', 
                '17 West Livingston Court'
                
            ]
        }
    )
    print(df)
    df["Words with a C"] = df["address"].str.findall(r"\b[A-Z].*?\b")
    print(df)
    

if __name__ == "__main__":
    main()