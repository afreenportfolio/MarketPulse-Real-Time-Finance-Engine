## Phase 1: Data Pipeline
1. I stored the daily stock data in a JSON file (with proper formatting to prevent formatting errors) to optimize API usage.
2. Developed a Python script that iterates through nested timeseries data to extract key metrics (Open, High, Low, Close, Volume)

### Challenge:
- Initial raw data was saved to the JSON file as one cramped line.
- Used indent=4 argument while "dumping" the JSON file to make the data human readable.
- Used "w" (write-only) argument to create the JSON file and to write to the JSON file.
- Used the "r" (read-only) argument to read and verify the data back from the file to the Python IDLE.

### Setup Instructions:
1. Rename the file name "local_file.json" (in the line "with open('local_file.json', 'r') as file:") with the name of the file which stores the daily stock data from the initial script run.
2. Run the Python script to fetch the key metrics through the nested timeseries
3. Your data pipeline is ready!
