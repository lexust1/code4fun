# Write a Pandas program to combine the columns of two potentially 
# differently-indexed DataFrames into a single result DataFrame.
import pandas as pd


def main():
    
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                        'B': ['B0', 'B1', 'B2']},
                        index=['K0', 'K1', 'K2'])
    
    df2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                        'D': ['D0', 'D2', 'D3']},
                        index=['K0', 'K2', 'K3'])
    
    print(df1, "\n")
    print(df2, "\n")
    
    df3 = df1.join(df2)
    print(df3, "\n")
    
    df4 = pd.merge(df1, df2, left_index=True, right_index=True, how="left")
    print(df4, "\n")

if __name__ == "__main__":
    main()