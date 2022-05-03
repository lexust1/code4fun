import pandas as pd

ds = pd.Series([[0, 1, 2], 
                [0, 1, 'python'], 
                ['Red', 'Green', 'Blue']])



ds_new = ds.apply(pd.Series).stack().reset_index(drop=True)