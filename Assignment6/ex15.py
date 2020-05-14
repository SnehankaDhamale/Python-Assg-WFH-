#Write a Python program to calculate product of digits of a number.

no=input("Enter the number:")
product=1
for i in no:
    product =product * int(i)
print("Product of number:",product)