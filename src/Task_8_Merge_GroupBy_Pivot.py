import pandas as pd

# Main dataset
sales = pd.read_csv("data/sales_data.csv")

# Second DataFrame
region_data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Manager": ["Amit", "Neha", "Rahul", "Priya"]
})

# -----------------------------
# MERGE
# -----------------------------

merged_df = pd.merge(
    sales,
    region_data,
    on="Region",
    how="left"
)

print("Merged DataFrame:")
print(merged_df)

# -----------------------------
# CONCATENATE
# -----------------------------

additional_sales = pd.DataFrame({
    "Order_ID": [1013, 1014],
    "Date": ["2026-03-12", "2026-03-15"],
    "Product": ["Tablet", "Office Chair"],
    "Category": ["Electronics", "Furniture"],
    "Region": ["North", "South"],
    "Sales": [25000, 8500],
    "Quantity": [2, 2],
    "Profit": [4000, 1300],
    "Customer": ["Manish", "Pooja"]
})

concatenated_df = pd.concat(
    [sales, additional_sales],
    ignore_index=True
)

print("\nConcatenated DataFrame:")
print(concatenated_df)

# -----------------------------
# GROUPBY
# -----------------------------

grouped_sales = sales.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:")
print(grouped_sales)

# Multiple aggregations
grouped_summary = sales.groupby("Region").agg({
    "Sales": ["sum", "mean", "max", "min"],
    "Profit": "sum"
})

print("\nRegional Summary:")
print(grouped_summary)

# -----------------------------
# PIVOT TABLE
# -----------------------------

pivot_table = pd.pivot_table(
    sales,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:")
print(pivot_table)