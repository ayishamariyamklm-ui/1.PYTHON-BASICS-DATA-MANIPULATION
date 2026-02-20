# 1️⃣ REMOVE DUPLICATES FROM A LIST

numbers = [10, 20, 20, 30, 40, 40, 50]

print("Original Numbers:", numbers)

def remove_duplicates(data):
    return list(set(data))

unique_numbers = remove_duplicates(numbers)
print("After Removing Duplicates:", unique_numbers)
print("\n")


# 2️⃣ REMOVE MISSING VALUES (None, Empty String)


raw_data = [10, None, 25, "", 40, None, 0, 55]

print("Raw Data:", raw_data)

def remove_missing(data):
    return [x for x in data if x not in (None, "")]

cleaned_data = remove_missing(raw_data)
print("After Removing Missing Values:", cleaned_data)
print("\n")


# 3️⃣ FILTER DATA BASED ON CONDITION


scores = [35, 78, 90, 45, 60, 30, 85]

print("Original Scores:", scores)

def filter_passing(scores, passing_mark=50):
    return [score for score in scores if score >= passing_mark]

passing_scores = filter_passing(scores)
print("Passing Scores:", passing_scores)
print("\n")


# 4️⃣ CLEAN STRING DATA (TRIM + LOWERCASE)


names = ["  AYISHA  ", "Mariyam", "  john", "SARA  "]

print("Original Names:", names)

def clean_names(data):
    return [name.strip().lower() for name in data]

cleaned_names = clean_names(names)
print("Cleaned Names:", cleaned_names)
print("\n")

# 5️⃣ CLEAN NUMERICAL DATA (REMOVE NEGATIVE VALUES)

temperatures = [25, -5, 30, -2, 28, 32]

print("Original Temperatures:", temperatures)

def remove_negative(data):
    return [value for value in data if value >= 0]

cleaned_temperatures = remove_negative(temperatures)
print("After Removing Negative Values:", cleaned_temperatures)
print("\n")


# 6️⃣ CLEAN DICTIONARY DATASET 

students = [
    {"name": "  Ayisha ", "age": 23, "score": 85},
    {"name": "Mariyam", "age": None, "score": 90},
    {"name": "john", "age": 21, "score": -10},
    {"name": "SARA  ", "age": 22, "score": 75},
    {"name": "  Ayisha ", "age": 23, "score": 85},  # duplicate
]

print("Original Student Data:")
for s in students:
    print(s)

def clean_student_data(data):
    cleaned = []
    seen = set()

    for student in data:
        name = student["name"].strip().title()
        age = student["age"]
        score = student["score"]

        # Remove missing age
        if age is None:
            continue

        # Remove invalid scores
        if score < 0:
            continue

        # Remove duplicates using tuple
        student_key = (name, age, score)
        if student_key in seen:
            continue

        seen.add(student_key)

        cleaned.append({
            "name": name,
            "age": age,
            "score": score
        })

    return cleaned

cleaned_students = clean_student_data(students)

print("\nCleaned Student Data:")
for s in cleaned_students:
    print(s)

print("\n")


# 7️⃣ COMPLETE CLEANING PIPELINE FUNCTION


def cleaning_pipeline(data):
    # Step 1: Remove None and empty
    step1 = [x for x in data if x not in (None, "")]

    # Step 2: Remove duplicates
    step2 = list(set(step1))

    # Step 3: Keep only numbers greater than 10
    step3 = [x for x in step2 if isinstance(x, int) and x > 10]

    return step3


mixed_data = [None, 5, 15, "", 20, 20, 8, 30]

print("Mixed Raw Data:", mixed_data)
final_cleaned = cleaning_pipeline(mixed_data)
print("Final Cleaned Data:", final_cleaned)

