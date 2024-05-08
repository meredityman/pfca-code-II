from pathlib import Path
import datetime as datetime
import os

def main():

    root_path = Path("./data")

    start_date = datetime.date(2024, 1, 1)
    end_date   = datetime.date.today()


    if( start_date >= end_date  ):
        raise ValueError("Start date must by earlier than end date")

    current_date = start_date
    while(current_date <= end_date):
        print(current_date)
        month    = current_date.strftime("%B")
        year     = current_date.strftime("%Y")
        day_name = current_date.strftime("%A")  
        day      = current_date.strftime("%d")  

        print(month, year, day_name, day)

        current_date += datetime.timedelta(days=1)








if __name__ == "__main__":
    main()