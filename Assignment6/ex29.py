#Write a Python program to print Pascal triangle upto n rows
'''def pascal_tri(n):
    for line in range(1,n+1):
        D=1
        for i in range(1,line+1):
            print (D) ,
            D=D*(line-i)/i
        print ("\n")

no=int(input("Enter the no of rows:"))
pascal_tri(no)'''
n=int(input("Enter the nos of rows:"))
a=[]#Empty list
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if n !=0:
        a[i].append(1)
for i in range (n):
    print(" "*(n-i),end=' ',sep=' ')
    for j in range(0,i+1):
        print(a[i][j],end=' ',sep=' ')
    print()