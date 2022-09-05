# Write a Pandas program to create a DataFrame using intervals as an index.

# IntervalIndex represents an Index of Interval objects that are all closed 
# on the same side.

# pandas.IntervalIndex.from_breaks: Construct an IntervalIndex from an array 
# of splits

# pandas.IntervalIndex.from_tuples: Construct an IntervalIndex from a 
# list/array of tuples

# pandas.IntervalIndex.from_arrays: Construct from two arrays defining the 
# left and right bounds.

import pandas as pd

df1 = pd.DataFrame(data={'X': [1, 2, 3, 4, 5, 6, 7],
                         'Y': [1, 2, 3, 4, 5, 6, 7]},
                   index=pd.IntervalIndex.from_breaks(
                       [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5]))
print(df1)

df2 = pd.DataFrame(data={'X': [1, 2, 3, 4, 5, 6, 7],
                         'Y': [1, 2, 3, 4, 5, 6, 7]},
                   index=pd.IntervalIndex.from_tuples(
                       [(0, 0.5), (0.5, 1.0), (1.0, 1.5), (1.5, 2.0), 
                        (2.0, 2.5), (2.5, 3.0), (3.0, 3.5)]))
print(df2)

df3 = pd.DataFrame(data={'X': [1, 2, 3, 4, 5, 6, 7],
                         'Y': [1, 2, 3, 4, 5, 6, 7]},
                   index=pd.IntervalIndex.from_arrays(
                       [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3],
                       [0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5]))
print(df3)