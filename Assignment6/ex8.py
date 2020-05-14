#Write a Python program to find sum of all odd numbers between 1 to n

n=int(input("Enter the no:"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=' ')#print all odd nos
        sum+=i
print("\nSum of all odd numbers:",sum)
