#Write a Python program to calculate factorial of a number.
no=int(input("Enter the number:"))
fact=1
for i in range(1,no+1):
    fact=fact*i #multiply from 1-no and return new value
print("Factorial of number:",fact)