import pandas as pd
import numpy as np

# ---------------------------------
# 1. Load Dataset
# ---------------------------------

df = pd.read_csv("data/sales_data.csv")

print("========== SALES DATA ANALYSIS ==========\n")

# ---------------------------------
# 2. Data Inspection
# ---------------------------------

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Information:")
print(df.dtypes)

# ---------------------------------
# 3. Check Missing Values
# ---------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------------
# 4. Statistical Analysis
# ---------------------------------

print("\nSales Statistics:")

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sale:", df["Sales"].max())
print("Minimum Sale:", df["Sales"].min())

print("\nTotal Profit:", df["Profit"].sum())
print("Average Profit:", df["Profit"].mean())

# ---------------------------------
# 5. Filtering
# ---------------------------------

high_sales = df[df["Sales"] > 10000]

print("\nOrders with Sales Greater Than 10,000:")
print(high_sales)

# ---------------------------------
# 6. Sorting
# ---------------------------------

sorted_sales = df.sort_values(
    "Sales",
    ascending=False
)

print("\nTop Sales Records:")
print(sorted_sales[[
    "Product",
    "Sales",
    "Profit"
]].head())

# ---------------------------------
# 7. GroupBy Analysis
# ---------------------------------

category_analysis = df.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
})

print("\nCategory Analysis:")
print(category_analysis)

region_analysis = df.groupby("Region").agg({
    "Sales": "sum",
    "Profit": "sum"
})

print("\nRegion Analysis:")
print(region_analysis)

# ---------------------------------
# 8. Pivot Table
# ---------------------------------

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nSales Pivot Table:")
print(pivot)

# ---------------------------------
# 9. NumPy Analysis
# ---------------------------------

sales_array = np.array(df["Sales"])

print("\nNumPy Analysis:")
print("Mean Sales:", np.mean(sales_array))
print("Median Sales:", np.median(sales_array))
print("Sales Standard Deviation:", np.std(sales_array))

# ---------------------------------
# 10. Export Cleaned Dataset
# ---------------------------------

output_file = "data/final_processed_sales_data.csv"

df.to_csv(output_file, index=False)

print("\nProcessed dataset exported to:")
print(output_file)

print("\n========== ANALYSIS COMPLETED ==========")