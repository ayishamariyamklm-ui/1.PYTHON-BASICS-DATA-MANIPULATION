# ===============================================
# CLIENT PROJECT: DATA VISUALIZATION DASHBOARD
# ===============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------
# 1. Load Dataset
# -----------------------------------------------

df = sns.load_dataset("tips")

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------------------------
# 2. Create Dashboard Layout
# -----------------------------------------------

plt.figure(figsize=(16, 10))

# -----------------------------------------------
# 3. Scatter Plot (Relationship)
# -----------------------------------------------

plt.subplot(2, 3, 1)
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.title("Total Bill vs Tip")

# -----------------------------------------------
# 4. Histogram (Distribution)
# -----------------------------------------------

plt.subplot(2, 3, 2)
plt.hist(df["total_bill"], bins=20)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")

# -----------------------------------------------
# 5. Box Plot (Category Comparison)
# -----------------------------------------------

plt.subplot(2, 3, 3)
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Total Bill by Day")

# -----------------------------------------------
# 6. Bar Plot (Aggregation)
# -----------------------------------------------

avg_tip = df.groupby("day")["tip"].mean()

plt.subplot(2, 3, 4)
plt.bar(avg_tip.index, avg_tip.values)
plt.title("Average Tip by Day")
plt.ylabel("Average Tip")

# -----------------------------------------------
# 7. Violin Plot (Distribution by Gender)
# -----------------------------------------------

plt.subplot(2, 3, 5)
sns.violinplot(x="sex", y="tip", data=df)
plt.title("Tip Distribution by Gender")

# -----------------------------------------------
# 8. Heatmap (Correlation Matrix)
# -----------------------------------------------

plt.subplot(2, 3, 6)
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

# -----------------------------------------------
# 9. Final Adjustments
# -----------------------------------------------

plt.tight_layout()
plt.suptitle("Restaurant Data Analysis Dashboard", fontsize=16, y=1.02)
plt.show()

print("Dashboard Created Successfully!")
