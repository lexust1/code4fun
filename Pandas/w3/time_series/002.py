# Write a Pandas program to create
# a) a specific date using timestamp.
# b) date and time using timestamp.
# c) a time adds in the current local date using timestamp.
# d) current date and time using timestamp.

import pandas as pd


def main():
    print(f"a: {pd.Timestamp('2016-11-10')}")
    print(f"b: {pd.Timestamp('2016-11-10 18:20')}")
    print(f"c: {pd.Timestamp('18:20')}")
    print(f"d: {pd.Timestamp('now')}")


if __name__ == "__main__":
    main()