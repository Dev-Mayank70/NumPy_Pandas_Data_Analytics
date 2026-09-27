import pandas as pd

df = pd.read_csv("data/sales_data.csv")

# Selecting specific columns
print("Product and Sales Columns:")
print(df[["Product", "Sales"]])

# Selecting specific rows
print("\nFirst Three Rows:")
print(df.iloc[:3])

# Filtering records
print("\nSales Greater Than 10000:")
print(df[df["Sales"] > 10000])

# Multiple conditions
print("\nElectronics with Sales Greater Than 10000:")
print(
    df[
        (df["Category"] == "Electronics") &
        (df["Sales"] > 10000)
    ]
)

# Ascending sorting
print("\nSales in Ascending Order:")
print(df.sort_values("Sales", ascending=True))

# Descending sorting
print("\nSales in Descending Order:")
print(df.sort_values("Sales", ascending=False))