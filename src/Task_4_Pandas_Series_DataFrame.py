import pandas as pd

# Creating a Pandas Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)

# Creating a DataFrame
data = {
    "Name": ["Rahul", "Priya", "Aman", "Neha", "Rohan"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

# Column names
print("\nColumn Names:")
print(df.columns)

# Index
print("\nDataFrame Index:")
print(df.index)

# Adding a new column
df["Grade"] = ["B", "A", "C", "A", "B"]

print("\nUpdated DataFrame:")
print(df)