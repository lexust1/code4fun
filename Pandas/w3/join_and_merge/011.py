# Write a Pandas program to create a new DataFrame based on existing series, 
# using specified argument and override the existing columns names.
import pandas as pd


def main():
    
    ds1 = pd.Series([0, 1, 2, 3], name="col1")
    ds2 = pd.Series([0, 2, 4, 6])
    ds3 = pd.Series([10, 20, 30 ,40], name="col3")
    print(ds1, "\n")
    print(ds2, "\n")
    print(ds3, "\n")

    df = pd.concat([ds1, ds2, ds3], 
                   axis=1, 
                   keys=["column1", "column2", "column3"])
    print(df)


if __name__ == "__main__":
    main()
