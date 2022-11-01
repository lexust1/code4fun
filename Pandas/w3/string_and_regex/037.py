# Write a Pandas program to extract only words from a given column of 
# a given DataFrame.
import pandas as pd


def main() -> None:
    
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
                '9910 Surrey Ave.',
                '92 N. Bishop Ave.',
                '9910 Golden Star Ave.', 
                '102 Dunbar St.', 
                '17 West Livingston Court'
                ]
        }
    )
    print(df)

    df["words"] = df["address"].str.findall("[a-zA-Z]+")
    print(df)         


if __name__=="__main__":
    main()
    
    