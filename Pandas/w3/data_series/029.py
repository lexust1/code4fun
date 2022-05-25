# Write a Pandas program to convert year-month string to dates adding 
# a specified day of the month.

import pandas as pd

list_of_months = ['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019']
list_of_dates = ['11 ' + el for el in list_of_months]

ds = pd.Series(list_of_dates)

ds_date_time = pd.to_datetime(ds)

ds_date = ds_date_time.dt.date

ds_date2 = pd.to_datetime(ds).dt.date