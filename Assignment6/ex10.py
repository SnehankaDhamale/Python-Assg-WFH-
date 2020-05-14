#Write a Python program to count number of digits in a number.

no=int(input("Enter the no:"))
cnt =0
while no>0:
 no=no//10 # floor division
 cnt += 1
print("Total no of digits in number:",cnt)