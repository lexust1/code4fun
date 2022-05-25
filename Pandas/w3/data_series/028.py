# Write a Pandas program to get the day of month, day of year, 
# week number and day of week from a given series of date strings.
from dateutil.parser import parse
import pandas as pd

ds = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', 
                '2016-04-12', '2019-04-06T11:20'])



res1 = ds.map(lambda dt: parse(dt))

res2 = pd.to_datetime(ds)

res_day = res2.dt.day

res_day_of_year = res2.dt.dayofyear

res_week_of_year = res2.dt.weekofyear

res_day_of_week = res2.dt.dayofweek

print(res_day)
print(res_day_of_year)
print(res_week_of_year)
print(res_day_of_week)