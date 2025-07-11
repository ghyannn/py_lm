def get_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0

# Input number of subjects
n = int(input("Enter number of subjects: "))

total_credits = 0
total_weighted_points = 0

for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    credit = int(input(f"Enter credit for subject {i+1}: "))
    
    grade_point = get_grade_point(marks)
    total_weighted_points += grade_point * credit
    total_credits += credit

# Calculate SPI
if total_credits > 0:
    spi = total_weighted_points / total_credits
    print("\nYour SPI is:", round(spi, 2))
else:
    print("Invalid total credits.")
