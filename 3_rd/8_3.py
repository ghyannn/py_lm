start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:  # Skip 1 and below
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
