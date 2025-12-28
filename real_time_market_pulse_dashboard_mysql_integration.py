import json
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Cretae the connection object
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
    )

cursor = conn.cursor()

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
    sql = """
    INSERT INTO ibm_daily_stock(trade_date, open_price, high_price, low_price, close_price, volume)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        open_price=VALUES(open_price),
        high_price=VALUES(high_price),
        low_price=VALUES(low_price),
        close_price=VALUES(close_price),
        volume=VALUES(volume)
    """
    cursor.execute(sql, (date, open_price, high_price, low_price, close_price, volume))

    # Save changes to the databse
    conn.commit()

# Close cursor and connection
cursor.close()
conn.close()

print("Data successfully uploaded to MySQL")
