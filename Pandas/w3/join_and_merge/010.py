# Write a Pandas program to merge two given datasets using multiple join keys.
import pandas as pd


def main():
    df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'P': ['P0', 'P1', 'P2', 'P3'],
                        'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
    
    df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'R': ['R0', 'R1', 'R2', 'R3'],
                        'S': ['S0', 'S1', 'S2', 'S3']})
    
    print(df1, "\n")
    print(df2, "\n")
    
    df3 = pd.merge(df1, df2, on=["key1", "key2"])
    print(df3, "\n")
    
    df4 = (
        df1.set_index(["key1", "key2"])
            .join(df2.set_index(["key1", "key2"]), how="inner")
    )
    print(df4, "\n")
    

if __name__ == "__main__":
    main()