# Write a Pandas program to Combine two DataFrame objects by filling null 
# values in one DataFrame with non-null values from other DataFrame.
import pandas as pd


def main():
    df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
    df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})
    
    print(df1, "\n")
    print(df2, "\n")

    df3 = df1.combine_first(df2)
    print(df3, "\n")

if __name__ == "__main__":
    main()