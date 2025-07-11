# Check age and print appropriate message

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("You are a Minor.")
elif age < 60:
    print("You are an Adult.")
elif age <= 120:
    print("You are a Senior Citizen.")
else:
    print("Invalid age")
