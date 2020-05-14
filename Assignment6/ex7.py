#Write a Python program to find sum of all even numbers between 1 to n
n =int(input("Enter the number:"))
sum=0

for i in range(1,n+1):
     if i % 2==0:
        print(i,end=' ') #prints all even no
        sum = sum + i   #addition
print("\n sum of even numbers:",sum)

