# SAMPLE DATA

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sales_data = [
    {"product": "Laptop", "price": 800, "quantity": 5},
    {"product": "Phone", "price": 500, "quantity": 10},
    {"product": "Tablet", "price": 300, "quantity": 7},
    {"product": "Headphones", "price": 100, "quantity": 15},
]

print("Original Numbers:", numbers)
print("Original Sales Data:", sales_data)
print("\n")


# 1️⃣ SUM OF SQUARES


def sum_of_squares(data):
    return sum(x ** 2 for x in data)

result = sum_of_squares(numbers)
print("1️⃣ Sum of Squares:", result)
print("\n")


# 2️⃣ FILTER EVEN NUMBERS


def filter_even(data):
    return [x for x in data if x % 2 == 0]

even_numbers = filter_even(numbers)
print("2️⃣ Even Numbers:", even_numbers)
print("\n")



# 3️⃣ FILTER NUMBERS GREATER THAN A VALUE


def filter_greater_than(data, threshold):
    return list(filter(lambda x: x > threshold, data))

greater_numbers = filter_greater_than(numbers, 5)
print("3️⃣ Numbers Greater Than 5:", greater_numbers)
print("\n")



# 4️⃣ DOUBLE ALL VALUES (TRANSFORMATION)


def double_values(data):
    return list(map(lambda x: x * 2, data))

doubled = double_values(numbers)
print("4️⃣ Doubled Values:", doubled)
print("\n")



# 5️⃣ TOTAL SALES PER PRODUCT (DICTIONARY TRANSFORMATION)


def calculate_total_sales(data):
    transformed = []
    for item in data:
        total = item["price"] * item["quantity"]
        transformed.append({
            "product": item["product"],
            "total_sales": total
        })
    return transformed

total_sales = calculate_total_sales(sales_data)
print("5️⃣ Total Sales Per Product:")
for item in total_sales:
    print(item)
print("\n")



# 6️⃣ TOTAL REVENUE (AGGREGATION)


def calculate_total_revenue(data):
    return sum(item["price"] * item["quantity"] for item in data)

total_revenue = calculate_total_revenue(sales_data)
print("6️⃣ Total Revenue:", total_revenue)
print("\n")



# 7️⃣ FILTER PRODUCTS ABOVE A CERTAIN PRICE


def filter_expensive_products(data, min_price):
    return [item for item in data if item["price"] > min_price]

expensive_products = filter_expensive_products(sales_data, 400)
print("7️⃣ Expensive Products (Price > 400):")
for item in expensive_products:
    print(item)
print("\n")



# 8️⃣ SORT PRODUCTS BY TOTAL SALES (DESCENDING)


def sort_by_total_sales(data):
    return sorted(
        data,
        key=lambda item: item["price"] * item["quantity"],
        reverse=True
    )

sorted_products = sort_by_total_sales(sales_data)
print("8️⃣ Products Sorted by Total Sales (High to Low):")
for item in sorted_products:
    print(item)
print("\n")



# 9️⃣ REMOVE DUPLICATES (SET TRANSFORMATION)


duplicate_numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original with Duplicates:", duplicate_numbers)

def remove_duplicates(data):
    return list(set(data))

unique_numbers = remove_duplicates(duplicate_numbers)
print("9️⃣ Unique Numbers:", unique_numbers)
print("\n")



# 🔟 DATA CLEANING EXAMPLE


raw_data = [10, None, 20, "", 30, 0, None, 40]

print("Raw Data:", raw_data)

def clean_data(data):
    return [x for x in data if x not in (None, "", 0)]

cleaned = clean_data(raw_data)
print("🔟 Cleaned Data:", cleaned)
print("\n")


# COMBINED TRANSFORMATION PIPELINE

def transformation_pipeline(data):
    # Step 1: Remove numbers less than 5
    step1 = [x for x in data if x >= 5]

    # Step 2: Square the numbers
    step2 = [x ** 2 for x in step1]

    # Step 3: Get sum
    result = sum(step2)

    return result

pipeline_result = transformation_pipeline(numbers)
print("Pipeline Result:", pipeline_result)


