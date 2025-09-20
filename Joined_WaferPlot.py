import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px

# Define the folder path
folder_path = r"C:\Users\ADVINCULA\OneDrive\Desktop\OwnMyOwn\9-15"

# Load the joined CSV file
joined_path = os.path.join(folder_path, "Joined_Wafer.csv")
joined_df = pd.read_csv(joined_path)

# Calculate the price difference
joined_df['Price_Diff'] = joined_df['Price_Wafer1'] - joined_df['Price_Wafer3']

# Create a histogram of the price difference
plt.figure(figsize=(10, 6))
joined_df['Price_Diff'].hist(bins=50)
plt.title('Histogram of Price Difference')
plt.xlabel('Price Difference')
plt.ylabel('Frequency')
plt.show()

# Create a scatter plot of the prices
plt.figure(figsize=(12, 8))
plt.scatter(joined_df['Timestamp'], joined_df['Price_Wafer1'], label='Wafer1', alpha=0.6)
plt.scatter(joined_df['Timestamp'], joined_df['Price_Wafer3'], label='Wafer3', alpha=0.6)
plt.title('Scatter Plot of Wafer Prices')
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Create a scatter plot of the price difference over time
plt.figure(figsize=(12, 6))
plt.scatter(joined_df['Timestamp'], joined_df['Price_Diff'])
plt.title('Scatter Plot of Price Difference Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Price Difference')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Optional: Convert timestamp to datetime for better plotting
try:
    joined_df['Timestamp'] = pd.to_datetime(joined_df['Timestamp'])
    
    # Create time series plots with proper datetime handling
    plt.figure(figsize=(12, 8))
    plt.plot(joined_df['Timestamp'], joined_df['Price_Wafer1'], label='Wafer1', alpha=0.7)
    plt.plot(joined_df['Timestamp'], joined_df['Price_Wafer3'], label='Wafer3', alpha=0.7)
    plt.title('Time Series Plot of Wafer Prices')
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Price difference over time as line plot
    plt.figure(figsize=(12, 6))
    plt.plot(joined_df['Timestamp'], joined_df['Price_Diff'])
    plt.title('Price Difference Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Price Difference')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
except Exception as e:
    print(f"Could not convert timestamp to datetime: {e}")
    print("Using original timestamp format for plotting")