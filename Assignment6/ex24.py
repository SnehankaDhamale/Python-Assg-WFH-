#Write a Python program to check whether a number is Prime number or not.

no=int(input("Enter the no:"))

for i in range(2,no+1):
      if no%i==0:
        print(no, "is not prime")
        break
else:#end of for
 print(no,"is prime no")
