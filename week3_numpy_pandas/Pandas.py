import pandas as pd

# 4️⃣ PANDAS SERIES

series = pd.Series([100, 200, 300], index=["A", "B", "C"])
print("Pandas Series:")
print(series)

print("\nAccess element with label 'A':", series["A"])


# 5️⃣ PANDAS DATAFRAME

data = {
    "Name": ["Ayisha", "Mariyam", "John", "Sara"],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Salary": [50000, 40000, 60000, 55000]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# 6️⃣ INDEXING


# Select single column
print("\nSelect 'Name' column:")
print(df["Name"])

# Select multiple columns
print("\nSelect Name and Salary:")
print(df[["Name", "Salary"]])

# Using .loc (label-based)
print("\nUsing .loc (Row 0):")
print(df.loc[0])

print("\nUsing .loc (Row 0, Name):")
print(df.loc[0, "Name"])

# Using .iloc (position-based)
print("\nUsing .iloc (Row 0):")
print(df.iloc[0])

print("\nUsing .iloc (Row 0, Column 2):")
print(df.iloc[0, 2])



# 7️⃣ FILTERING DATA


print("\nEmployees with Salary > 50000:")
high_salary = df[df["Salary"] > 50000]
print(high_salary)



# 8️⃣ GROUPING DATA (GROUPBY)


print("\nAverage Salary by Department:")
grouped_mean = df.groupby("Department")["Salary"].mean()
print(grouped_mean)

print("\nTotal Salary by Department:")
grouped_sum = df.groupby("Department")["Salary"].sum()
print(grouped_sum)

print("\nCount by Department:")
grouped_count = df.groupby("Department")["Salary"].count()
print(grouped_count)