import pandas as pd
import numpy as np



# 1️⃣ RAW CLIENT DATA (Simulating CSV Import)


data = {
    "OrderID": [101, 102, 103, 104, 105, 101],  # duplicate OrderID 101
    "Customer": ["  Ayisha", "Mariyam", "John", "Sara", None, "  Ayisha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Sales": [5000, 7000, None, 6000, 8000, 5000],
    "Quantity": [5, 7, 6, None, 8, 5]
}

df = pd.DataFrame(data)

print("🔹 Raw Dataset:\n")
print(df)


# 2️⃣ REMOVE DUPLICATES


df = df.drop_duplicates(subset="OrderID")

print("\n🔹 After Removing Duplicates:\n")
print(df)


# 3️⃣ HANDLE MISSING VALUES


# Remove rows with missing Customer name
df = df.dropna(subset=["Customer"])

# Replace missing Sales with mean Sales
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

# Replace missing Quantity with median Quantity
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

print("\n🔹 After Handling Missing Values:\n")
print(df)



# 4️⃣ CLEAN TEXT FIELDS


df["Customer"] = df["Customer"].str.strip().str.title()

print("\n🔹 After Cleaning Customer Names:\n")
print(df)



# 5️⃣ FILTER INVALID RECORDS


# Remove records where Sales <= 0
df = df[df["Sales"] > 0]

print("\n🔹 After Filtering Invalid Sales:\n")
print(df)



# 6️⃣ CREATE NEW COLUMN (TOTAL REVENUE)


df["TotalRevenue"] = df["Sales"] * df["Quantity"]

print("\n🔹 After Adding Total Revenue Column:\n")
print(df)


# 7️⃣ AGGREGATION - CALCULATE AVERAGES


# Average Sales
avg_sales = df["Sales"].mean()
print("Average Sales:", avg_sales)

# Total Revenue
total_revenue = df["TotalRevenue"].sum()
print("Total Revenue:", total_revenue)

# Average Revenue per Department
avg_revenue_dept = df.groupby("Department")["TotalRevenue"].mean()
print("\nAverage Revenue by Department:\n")
print(avg_revenue_dept)

# Total Revenue by Department
total_revenue_dept = df.groupby("Department")["TotalRevenue"].sum()
print("\nTotal Revenue by Department:\n")
print(total_revenue_dept)


# 8️⃣ SORT RESULTS


sorted_df = df.sort_values(by="TotalRevenue", ascending=False)

print("\n🔹 Top Performing Orders:\n")
print(sorted_df)