num = int(input("Enter a number: "))


for i in range(2,num+1,1): #staring from 2 since 1 will be the smallest divisor always
    if num %i==0:
        smallest=i
        break


for i in range(num-1,0,-1):# endig at a number ahead so that it is not the largest diviosr
    if num % i == 0:
        largest = i
        break


print("The smallest divisor is:", smallest)
print("The largest divisor is:", largest) 