#Star pattern programs - Write a Python program to print the given star patterns
'''#RightAngle triangle
n=int(input("Enter no of rows:"))
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end=' ')
    print()
'''

#Pyramid
n=int(input("Enter no of rows:"))
for i  in range(0,n+1):
    for j in range(0,n-i-1):
        print(end=' ')
    for j in range(0,i+1):
        print("*",end=' ')
    print()
