#Write a Python program to print multiplication table of any number.

no=int(input("Enter the number:"))
print("Multiplication table of ",no)
for i in range(1,11):
    no1=no*i
    print(no1,end=' ')
