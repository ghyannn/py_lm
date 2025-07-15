str=input("enter the string: ")

count=0
vowel="aeiouAEIOU"
for char in str:
    if char in vowel:
        count+=1

print("the number of vowels is : ",count)