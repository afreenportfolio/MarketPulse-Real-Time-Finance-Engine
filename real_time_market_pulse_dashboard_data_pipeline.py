import json
import mysql.connector

#Opening the local file instead of the API
with open('data.json', 'r') as file:
    data = json.load(file)

#Getting the dictionary of daily record
daily_records = data['Time Series (Daily)']

#Turning the keys (dates) into a list
all_dates = list(daily_records.keys())

for date in all_dates:

    #1. Get the dictionary for this specific date:
    stats = daily_records[date]

    #2. Extract the open price:
    open_price = stats['1. open']

    #3. Extract the close price:
    high_price = stats['2. high']

    #4. Extract the high price:
    low_price = stats['3. low']

    #5. Extract the close price:
    close_price = stats['4. close']

    #6. Extract the volume:
    volume = stats['5. volume']
    print(f"{date}: \nOpen was {open_price}\nHigh was {high_price}\nLow was {low_price}\nClose was {close_price}\nVolume was {volume}\n")

