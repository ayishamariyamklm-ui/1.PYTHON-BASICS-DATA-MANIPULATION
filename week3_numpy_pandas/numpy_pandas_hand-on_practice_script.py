import numpy as np
import pandas as pd


# Create NumPy array (monthly sales)
sales = np.array([20000, 25000, 22000, 27000, 30000, 28000])

print("Monthly Sales:", sales)

# Basic operations
print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))
print("Minimum Sales:", np.min(sales))

# Increase all sales by 10% using broadcasting
updated_sales = sales * 1.10
print("\nSales After 10% Increase:", updated_sales)

# Normalize sales (scaling)
normalized_sales = (sales - np.mean(sales)) / np.std(sales)
print("\nNormalized Sales:", normalized_sales)


# Create dataset
data = {
    "Employee": ["Ayisha", "Mariyam", "John", "Sara", "Ali", "Omar"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [60000, 45000, 70000, 50000, 48000, 75000],
    "Experience": [3, 5, 4, 2, 6, 7]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)



# 1️⃣ ADD NEW COLUMN


# Add bonus column (10% of salary)
df["Bonus"] = df["Salary"] * 0.10

print("\nDataset After Adding Bonus Column:\n")
print(df)



# 2️⃣ FILTER DATA


# Employees with salary above 60000
high_salary = df[df["Salary"] > 60000]

print("\nEmployees with Salary > 60000:\n")
print(high_salary)


# 3️⃣ SORT DATA


sorted_df = df.sort_values(by="Salary", ascending=False)

print("\nEmployees Sorted by Salary (High to Low):\n")
print(sorted_df)



# 4️⃣ GROUPING & AGGREGATION

# Average salary by department
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:\n")
print(avg_salary)

# Total salary by department
total_salary = df.groupby("Department")["Salary"].sum()

print("\nTotal Salary by Department:\n")
print(total_salary)



# 5️⃣ APPLY CUSTOM FUNCTION


def categorize_experience(years):
    if years >= 6:
        return "Senior"
    elif years >= 3:
        return "Mid-Level"
    else:
        return "Junior"

df["Level"] = df["Experience"].apply(categorize_experience)

print("\nDataset After Adding Experience Level:\n")
print(df)



# 6️⃣ INDEXING


print("\nSelect Only Salary Column:\n")
print(df["Salary"])

print("\nSelect First 3 Rows:\n")
print(df.iloc[:3])

print("\nSelect Specific Columns:\n")
print(df[["Employee", "Salary", "Level"]])


# 7️⃣ SUMMARY STATISTICS


print("\nSummary Statistics:\n")
print(df.describe())