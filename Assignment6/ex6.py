# Write a Python program to find sum of all natural numbers between 1 to n.
'''
no=int(input("Enter the positive no:"))
sum=0
for i in range(no,0,-1):   #by using for loop
    sum+=no
    no -=1

print("Sum of natural nos are:",sum)'''

no=int(input("Enter the positive no:"))
if no <0:
    print("please Enter the positive number")
else:
    sum = 0
    while no>0 :
        sum += no
        no -= 1
print("Sum of natural nos are:",sum)

