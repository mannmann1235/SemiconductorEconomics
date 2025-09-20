import pandas as pd
import os

# Define the folder path
folder_path = r"C:\Users\ADVINCULA\OneDrive\Desktop\OwnMyOwn\9-15"

# Load the CSV files
wafer1_path = os.path.join(folder_path, "Wafer1.csv")
wafer3_path = os.path.join(folder_path, "Wafer3.csv")

wafer1_df = pd.read_csv(wafer1_path)
wafer3_df = pd.read_csv(wafer3_path)

# Ensure the Timestamp column is in datetime format
wafer1_df['Timestamp'] = pd.to_datetime(wafer1_df['Timestamp'])
wafer3_df['Timestamp'] = pd.to_datetime(wafer3_df['Timestamp'])

# Join the DataFrames on the Timestamp column
joined_df = pd.merge(wafer1_df, wafer3_df, on='Timestamp', suffixes=('_Wafer1', '_Wafer3'))

# Save the joined DataFrame to a new CSV file
joined_path = os.path.join(folder_path, "Joined_Wafer.csv")
joined_df.to_csv(joined_path, index=False)

print(f"Joined data saved to Joined_Wafer.csv in {folder_path}")