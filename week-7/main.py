import argparse
from datetime import datetime
import requests
import json

def main(args):

    try:
        date = datetime.strptime(args.date, "%Y-%m-%d")  
    except ValueError:
        print("Date is incorrect format!")
        return
    print(f"Parsed date {date}!")
    
    formatted_date = datetime.strftime(date, "%Y-%m-%d")

    url = f"https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date={formatted_date}&end_date={formatted_date}&daily=temperature_2m_mean,precipitation_sum&timezone=Europe%2FBerlin"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            print(json.dumps(weather_data, indent=4))
        else:
            print(f"Request failed with code {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Connection error")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather Getter")
    parser.add_argument("date", help="The date to retrieve weather info for")

    args = parser.parse_args()
    main(args)