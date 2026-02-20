import numpy as np


# 1️⃣ NUMPY ARRAYS

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# Shape and dimensions
print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)


# 2️⃣ NUMPY OPERATIONS


a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\nArray A:", a)
print("Array B:", b)

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("\nMean:", np.mean(a))
print("Sum:", np.sum(a))
print("Max:", np.max(a))
print("Min:", np.min(a))

# 3️⃣ BROADCASTING

print("\nBroadcasting Example:")

arr = np.array([1, 2, 3])
print("Original Array:", arr)

# Scalar broadcasting
print("Add 10:", arr + 10)

# Broadcasting with 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

vector = np.array([10, 20, 30])

print("\nMatrix:")
print(matrix)

print("\nVector:")
print(vector)

print("\nMatrix + Vector (Broadcasting):")
print(matrix + vector)