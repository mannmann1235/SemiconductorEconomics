import requests
import pandas as pd
import os

# Define the API endpoint and parameters
url = "https://api.coingecko.com/api/v3/coins/ibm-ondo-tokenized-stock/market_chart"
params = {
    "vs_currency": "usd",
    "days": "365",
    "interval": "daily"
}

# Send a GET request to the API endpoint
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Extract the prices and timestamps
    prices = data["prices"]

    # Create a pandas DataFrame from the prices data
    df = pd.DataFrame(prices, columns=["Timestamp", "Price"])

    # Convert the timestamp to a datetime object
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

    # Define the folder path
    folder_path = r"C:\Users\ADVINCULA\OneDrive\Desktop\OwnMyOwn\9-15"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the DataFrame to a CSV file
    file_path = os.path.join(folder_path, "Wafer1.csv")
    df.to_csv(file_path, index=False)

    print(f"Data saved to Wafer1.csv in {folder_path}")
else:
    print("Failed to retrieve data.")
    