# Write a Pandas program to use a local variable within a query.
import pandas as pd

df = pd.DataFrame({'W':[68,75,86,80,66],
                   'X':[78,85,96,80,86], 
                   'Y':[84,94,89,83,86],
                   'Z':[86,97,96,72,83]});

max_in_W = df["W"].max()
print(max_in_W)

print(df[df["W"] < max_in_W])

print(df.query("W < @max_in_W"))

