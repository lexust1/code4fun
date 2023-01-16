# Write a Pandas program to create a date from a given year, month, day 
# and another date from a given string formats.
from datetime import datetime
from dateutil import parser


def main():
    
    date1 = datetime(year=2023, month=1, day=10)
    print(f"a: {date1}")
    
    date_str = "1st of January, 2023"
    date2 = parser.parse(date_str)
    print(f"b: {date2}")
    

if __name__ == "__main__":
    main()

