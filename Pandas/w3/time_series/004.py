# Write a Pandas program to print the day after and before a specified date. 
# Also print the days between two given dates.
import pandas as pd
from datetime import datetime


def main():
    
    today_date = pd.to_datetime("2023-01-10")
    print(f"Today: {today_date}")
    
    tommorow_date = today_date + pd.Timedelta(days=1)
    print(f"Tommorow: {tommorow_date}")
    
    yesterday_date = today_date - pd.Timedelta(days=1)
    print(f"Yesterday: {yesterday_date}")

if __name__ == "__main__":
    main()

