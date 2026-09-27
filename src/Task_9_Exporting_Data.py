import pandas as pd

# Read dataset
df = pd.read_csv("data/sales_data.csv")

# Example processing
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

# Export processed data
output_file = "data/processed_sales_data.csv"

df.to_csv(output_file, index=False)

print("Processed data exported successfully.")
print("File:", output_file)

# Verify exported file
verified_df = pd.read_csv(output_file)

print("\nExported Data:")
print(verified_df.head())

print("\nExported file shape:", verified_df.shape)