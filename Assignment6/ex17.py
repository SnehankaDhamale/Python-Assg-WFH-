#Write a Python program to check whether a number is palindrome or not.
no=int(input("Enter the no:"))
no1=0
temp=no
while no>0:
    rem=no %10
    no1=(no1*10)+rem
    no =no//10

if temp == no1:
 print("Number",temp," is Palindrome")
else:
 print("Number",temp," is not palindrome")
