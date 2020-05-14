#Write a program which can compute the factorial of a given numbers.

no=input("Enter the no:")
fact=1
for i in range(1,int(no)+1): #need to typecast no else it consider as string
    fact=fact*i

print("Factorial:",fact)