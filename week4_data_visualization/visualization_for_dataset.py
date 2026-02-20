import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------

df = sns.load_dataset("tips")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# ------------------------------------------
# 2. Basic Analysis
# ------------------------------------------

# Average tip by day
avg_tip_day = df.groupby("day")["tip"].mean()
print("\nAverage Tip by Day:")
print(avg_tip_day)

# ------------------------------------------
# 3. Matplotlib Visualizations
# ------------------------------------------

# 1️⃣ Line Plot - Average Tip by Day
plt.figure(figsize=(6,4))
avg_tip_day.plot(kind="line")
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.grid(True)
plt.show()


# 2️⃣ Bar Plot - Average Total Bill by Day
avg_bill_day = df.groupby("day")["total_bill"].mean()

plt.figure(figsize=(6,4))
plt.bar(avg_bill_day.index, avg_bill_day.values)
plt.title("Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill")
plt.show()


# 3️⃣ Histogram - Distribution of Total Bill
plt.figure(figsize=(6,4))
plt.hist(df["total_bill"], bins=20)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()


# ------------------------------------------
# 4. Seaborn Visualizations
# ------------------------------------------

# 4️⃣ Scatter Plot - Total Bill vs Tip
plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total Bill vs Tip")
plt.show()


# 5️⃣ Box Plot - Total Bill by Day
plt.figure(figsize=(6,4))
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Total Bill by Day")
plt.show()


# 6️⃣ Violin Plot - Tip by Gender
plt.figure(figsize=(6,4))
sns.violinplot(x="sex", y="tip", data=df)
plt.title("Tip Distribution by Gender")
plt.show()


# 7️⃣ Heatmap - Correlation Matrix
plt.figure(figsize=(6,4))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 8️⃣ Pairplot - Relationship Between Variables
sns.pairplot(df, hue="sex")
plt.show()


# ------------------------------------------
# 5. Save a Plot 
# ------------------------------------------

plt.figure(figsize=(6,4))
sns.barplot(x="day", y="tip", data=df)
plt.title("Average Tip by Day")
plt.savefig("average_tip_by_day.png")
plt.show()
