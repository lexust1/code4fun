# Write a Pandas program to divide a DataFrame in a given ratio.

# Sample data:
    
# Original DataFrame:
# 0 1
# 0 0.316147 -0.767359
# 1 -0.813410 -2.522672
# 2 0.869615 1.194704
# 3 -0.892915 -0.055133
# 4 -0.341126 0.518266
# 5 1.857342 1.361229
# 6 -0.044353 -1.205002
# 7 -0.726346 -0.535147
# 8 -1.350726 0.563117
# 9 1.051666 -0.441533

# 70% of the said DataFrame:
# 0 1
# 8 -1.350726 0.563117
# 2 0.869615 1.194704
# 5 1.857342 1.361229
# 6 -0.044353 -1.205002
# 3 -0.892915 -0.055133
# 1 -0.813410 -2.522672
# 0 0.316147 -0.767359

# 30% of the said DataFrame:
# 0 1
# 4 -0.341126 0.518266
# 7 -0.726346 -0.535147
# 9 1.051666 -0.441533

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(10, 2))

print(df)

df_new = df.sample(frac=0.7)

print(df_new)