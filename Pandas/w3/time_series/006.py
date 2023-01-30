# Write a Pandas program to create a time-series from a given list of
# dates as strings.
import numpy as np
import pandas as pd


def main():
    dates = ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]
    ts = pd.Series(
        data=np.random.rand(4),
        index=dates
    )
    print(ts)
    print(type(ts.index))


if __name__ == "__main__":
    main()