# Write a Pandas program to join (left join) the two dataframes using keys 
# from left dataframe only.
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
    
    df3 = pd.merge(df1, df2, on=["key1", "key2"], how="left")
    print(df3, "\n")
    
    df31 = pd.merge(
        df1.set_index(["key1", "key2"]),
        df2.set_index(["key1", "key2"]),
        left_on=["key1", "key2"],
        right_on=["key1", "key2"],
        how="left"
    )
    print(df31, "\n")
    
    df4 = df1.join(df2.set_index(["key1", "key2"]), on=["key1", "key2"])
    print(df4, "\n")
    
    df5 = df1.set_index(["key1", "key2"]).join(df2.set_index(["key1", "key2"]))
    print(df5, "\n")
    
    df6 = df1.set_index(
        ["key1", "key2"]).join(df2.set_index(["key1", "key2"]), 
                               on=["key1", "key2"]
    )
    print(df6, "\n")
      
    df7 = df1.join(df2, lsuffix="_df1", rsuffix="_df2", how = "left")
    print(df7, "\n")  
     

if __name__ == "__main__":
    main()