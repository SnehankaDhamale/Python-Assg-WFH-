#Write a Python program to print all odd number between 1 to 100.

no=range(1,101)
odd_no=list(filter(lambda x:x%2!=0,no))
print("Odd Numbers from 1 to 100:\n",odd_no)