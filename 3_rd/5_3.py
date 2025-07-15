num = int(input("Enter a number: "))
is_negative = num < 0
num = abs(num)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if is_negative:
    reverse = -reverse

print("Reversed number:", reverse)
