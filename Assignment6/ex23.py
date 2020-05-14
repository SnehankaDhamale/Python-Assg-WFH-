#Write a Python program to find LCM of two numbers.

no1=float(input("Enter the first number:"))
no2=float(input("Enter the second number:"))
if no1>no2: #calculate max from both nos
    max=no1
else:
    max=no2

while True: #iterate
    if max %no1==0 and max%no2 ==0:
        print("LCM of",no2,"and",no2,"is:",max)
        break 
    max=max+1 #increased by 1 each time to get LCM