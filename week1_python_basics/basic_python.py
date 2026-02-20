# Variables are containers for storing data values
name = "John"           # String variable
age = 25               # Integer variable
height = 5.9           # Float variable
is_student = True      # Boolean variable

print(name)

# Basic Data Types
text = "Hello World"        # String (str)
number = 42                 # Integer (int)
decimal = 3.14             # Float (float)
flag = True                # Boolean (bool)
items = [1, 2, 3]          # List (list)
coordinates = (10, 20)     # Tuple (tuple)
student_info = {"name": "Alice", "age": 20}  # Dictionary (dict)

# Check data type
print(type(text))          

# Arithmetic Operators
a, b = 10, 3
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation

# Comparison Operators
print(a > b)    # Greater than
print(a < b)    # Less than
print(a == b)   # Equal to
print(a != b)   # Not equal to

# Logical Operators
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Output to console
print("Hello,", name)
print(f"You are {age} years old")  # f-string formatting
print("Age in 5 years:", age + 5)

# Basic if-else structure
temperature = float(input("Enter temperature: "))

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm")
elif temperature > 10:
    print("It's cool")
else:
    print("It's cold!")

# Nested conditions
age = int(input("Enter age: "))
if age >= 18:
    if age >= 65:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")


# For loop
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# For loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop
count = 1
print("While loop counting:")
while count <= 5:
    print(count)
    count += 1

# Loop with break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)    