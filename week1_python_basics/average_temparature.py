# Average Temperature Calculator
# This script calculates the average temperature from daily readings

print("=== Average Temperature Calculator ===")
print("Enter daily temperatures (enter 'done' when finished)")

temperatures = []
day = 1

while True:
    temp_input = input(f"Enter temperature for day {day} (or 'done' to finish): ")
    
    if temp_input.lower() == 'done':
        break
    
    try:
        temperature = float(temp_input)
        temperatures.append(temperature)
        day += 1
    except ValueError:
        print("Please enter a valid number or 'done'")

if temperatures:
    # Calculate statistics
    total_days = len(temperatures)
    total_temp = sum(temperatures)
    average_temp = total_temp / total_days
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    
    # Display results
    print("\n=== Temperature Analysis ===")
    print(f"Total days recorded: {total_days}")
    print(f"Average temperature: {average_temp:.2f}°")
    print(f"Highest temperature: {max_temp}°")
    print(f"Lowest temperature: {min_temp}°")
    print(f"Temperature range: {max_temp - min_temp}°")
    
    # Temperature classification
    if average_temp > 30:
        classification = "Hot"
    elif average_temp > 20:
        classification = "Warm"
    elif average_temp > 10:
        classification = "Cool"
    else:
        classification = "Cold"
    
    print(f"Average temperature classification: {classification}")
    
    # Display all temperatures
    print("\nDaily temperatures:")
    for i, temp in enumerate(temperatures, 1):
        print(f"Day {i}: {temp}°")
else:
    print("No temperatures were entered.")