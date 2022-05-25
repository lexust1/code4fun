# Write a Pandas program to compute the Euclidean distance between 
# two given series.

# Euclidean distance
# From Wikipedia, In mathematics, the Euclidean distance or Euclidean metric 
# is the "ordinary" straight-line distance between two points 
# in Euclidean space.  

# With this distance, Euclidean space becomes a metric space. 
# The associated norm is called the Euclidean norm.

import pandas as pd

x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

res = sum((x - y) ** 2) ** (1/2)

