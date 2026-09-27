import pandas as pd

df = pd.read_csv("data/sales_data_missing.csv")

print("Dataset Before Handling Missing Values:")
print(df)

# Identify missing values
print("\nMissing Value Matrix:")
print(df.isnull())

# Count missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Remove rows containing missing values
df_dropped = df.dropna()

print("\nDataset After Removing Rows with Missing Values:")
print(df_dropped)

# Fill missing values
df_filled = df.copy()

df_filled["Sales"] = df_filled["Sales"].fillna(df_filled["Sales"].mean())
df_filled["Quantity"] = df_filled["Quantity"].fillna(
    df_filled["Quantity"].median()
)
df_filled["Profit"] = df_filled["Profit"].fillna(
    df_filled["Profit"].mean()
)

print("\nDataset After Filling Missing Values:")
print(df_filled)