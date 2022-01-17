# 3. 
# Write a Python program to display the current date and time.


import datetime

now = datetime.datetime.now()
now_f = now.strftime("%Y-%m-%d %H:%M:%S")
date_and_time = "The current date and time: {now}".format(now=now_f)

print(date_and_time)
