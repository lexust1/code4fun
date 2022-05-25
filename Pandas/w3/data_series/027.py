# Write a Pandas program to convert a series of date strings to a timeseries.

import pandas as pd
# date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])

ds_str = pd.Series(['01 Jan 2022', 
                    '14-02-2022', 
                    #'10022022', 
                    '20220214', 
                    '2022/05/30', 
                    '2022-05-30', 
                    #'2022-30-05', 
                    #'2022/30/05',
                    '2020-04-14T11:20'])

ds_ts = pd.to_datetime(ds_str)

print(ds_ts)