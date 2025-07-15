num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
num3=int(input("enter 3rd number: "))

numbers=[num1,num2,num3]
for i in numbers:
    for j in numbers:
        for k in numbers:
            print(i,j,k)
