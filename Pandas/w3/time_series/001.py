# Write a Pandas program to create
# a) Datetime object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# f) Time from a datetime.
# g) Current local time.
import pandas as pd
import datetime
from datetime import datetime


def main():
        
    print(f"a: {datetime(2012, 1, 15)}\n")
    print(f"b: {datetime(2012, 1, 15, 21, 20)}\n")
    print(f"c: {datetime.now()}\n")
    print(f"d: {datetime(2012, 1, 15)}\n")
    
    
if __name__ == "__main__":
    main()