import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Define the folder path
folder_path = r"C:\Users\ADVINCULA\OneDrive\Desktop\OwnMyOwn\9-15"

# Load the joined CSV file
joined_path = os.path.join(folder_path, "Joined_Wafer.csv")
joined_df = pd.read_csv(joined_path)

# Calculate the price difference
joined_df['Price_Diff'] = joined_df['Price_Wafer1'] - joined_df['Price_Wafer3']

# Convert Timestamp if possible
try:
    joined_df['Timestamp'] = pd.to_datetime(joined_df['Timestamp'])
except Exception as e:
    print(f"Warning: Could not convert timestamp: {e}")

# -------------------------------
# 1. Interactive Histogram
# -------------------------------
fig1 = px.histogram(
    joined_df,
    x="Price_Diff",
    nbins=50,
    title="Histogram of Price Difference",
    labels={"Price_Diff": "Price Difference ($)", "count": "Frequency"}
)
fig1.update_traces(hovertemplate="Price Diff: %{x}<br>Frequency: %{y}<extra></extra>")
fig1.show()

# -------------------------------
# 2. Scatter plot of Wafer Prices
# -------------------------------
fig2 = px.scatter(
    joined_df,
    x="Timestamp",
    y=["Price_Wafer1", "Price_Wafer3"],
    title="Scatter Plot of Wafer Prices",
    labels={"value": "Price", "variable": "Wafer"}
)
fig2.update_traces(mode="markers", opacity=0.7)
fig2.show()

# -------------------------------
# 3. Scatter plot of Price Diff over time
# -------------------------------
fig3 = px.scatter(
    joined_df,
    x="Timestamp",
    y="Price_Diff",
    title="Scatter Plot of Price Difference Over Time",
    labels={"Price_Diff": "Price Difference ($)"}
)
fig3.update_traces(mode="markers", hovertemplate="Time: %{x}<br>Price Diff: %{y}<extra></extra>")
fig3.show()

# -------------------------------
# 4. Time Series Plot of Wafer Prices
# -------------------------------
fig4 = px.line(
    joined_df,
    x="Timestamp",
    y=["Price_Wafer1", "Price_Wafer3"],
    title="Time Series Plot of Wafer Prices",
    labels={"value": "Price", "variable": "Wafer"}
)
fig4.show()

# -------------------------------
# 5. Line Plot of Price Difference Over Time
# -------------------------------
fig5 = px.line(
    joined_df,
    x="Timestamp",
    y="Price_Diff",
    title="Price Difference Over Time",
    labels={"Price_Diff": "Price Difference ($)"}
)
fig5.update_traces(hovertemplate="Time: %{x}<br>Price Diff: %{y}<extra></extra>")
fig5.show()
