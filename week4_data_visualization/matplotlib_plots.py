import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create data
x = np.linspace(0, 10, 100)
y = x ** 2

# line Plot
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

#bar plot
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

plt.bar(categories, values)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

#histogram

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

#scatter plot

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#pie plot

sizes = [40, 30, 20, 10]
labels = ['Python', 'Java', 'C++', 'JavaScript']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
