#Write a Python program to calculate sum of digits of a number

no=input("Enter the no:") #take ip as string
sum=0
for i in no:
    sum=sum + int(i) #convert char into int
print("Sum of digits:",sum)