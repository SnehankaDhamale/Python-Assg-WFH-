#Write a Python program to check whether a number is Armstrong number or not
num=input("Enter the no:")
power=len(num) #calculate power i.e no of digits
num=int(num) #convert str to no
sum=0
temp=num
while temp>0:
    digit=temp %10 #calculate last digit
    sum=sum + digit ** power #calculate sum of digits with power
    temp=temp//10 #calculate new no

if num == sum:
    print(num,"is Armstrong Number")
else:
    print(num,"is not Armstrong number")