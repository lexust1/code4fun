# Write a Pandas program to create a time-series with two index labels
# and random values. Also print the type of the index.
import numpy as np
import pandas as pd


def main():
    ts = pd.Series(
        data=np.random.randn(2),
        index=[pd.to_datetime("2023-01-03"), pd.to_datetime("2023-01-05")]
    )
    print(ts)
    print(type(ts.index))


if __name__ == "__main__":
    main()
