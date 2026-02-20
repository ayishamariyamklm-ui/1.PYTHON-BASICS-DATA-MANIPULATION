# 1️⃣ LISTS

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Add element
numbers.append(60)
print("After append:", numbers)

# Insert element
numbers.insert(1, 15)
print("After insert:", numbers)

# Remove element
numbers.remove(30)
print("After remove:", numbers)

# Loop through list
print("Looping through list:")
for num in numbers:
    print(num)

print("\n")



# 2️⃣ TUPLES

coordinates = (10, 20, 30)

print("Tuple:", coordinates)
print("First value:", coordinates[0])

# Tuples are immutable (cannot modify)
# coordinates[0] = 100  ❌ This will cause error

print("\n")



# 3️⃣ DICTIONARIES

student = {
    "name": "Ayisha",
    "age": 23,
    "course": "Data Science"
}

print("Dictionary:", student)
print("Student Name:", student["name"])

# Add new key
student["grade"] = "A"
print("After adding grade:", student)

# Update value
student["age"] = 24
print("After updating age:", student)

# Loop through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

print("\n")



# 4️⃣ SETS

my_set = {1, 2, 3, 4, 4, 5}  # Duplicate 4 will be removed
print("Set:", my_set)

# Add element
my_set.add(6)
print("After add:", my_set)

# Remove element
my_set.remove(2)
print("After remove:", my_set)

print("\n")



# 5️⃣ FUNCTIONS

def greet(name):
    return f"Hello, {name}!"

print(greet("Ayisha"))

def add(a, b):
    return a + b

print("Addition:", add(10, 5))

print("\n")



# 6️⃣ LAMBDA FUNCTIONS

# Normal function
def square(x):
    return x * x

print("Square using normal function:", square(5))

# Lambda function
square_lambda = lambda x: x * x
print("Square using lambda:", square_lambda(5))

# Lambda with multiple arguments
multiply = lambda a, b: a * b
print("Multiply using lambda:", multiply(3, 4))

print("\n")



# 7️⃣ RECURSION

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

print("\n")



# 8️⃣ LIST COMPREHENSION

# Normal way
squares = []
for i in range(1, 6):
    squares.append(i * i)

print("Squares (normal loop):", squares)

# Using list comprehension
squares_comp = [i * i for i in range(1, 6)]
print("Squares (list comprehension):", squares_comp)

# With condition
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", even_numbers)

print("\n")



# Combining Concepts

numbers = [1, 2, 3, 4, 5]

# Using lambda + map
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)

# Using lambda + filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", evens)


