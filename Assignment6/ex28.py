#Write a Python program to print Fibonacci series up to n terms
num=int(input("Enter the no:"))
n1=0
n2=1 #first 2 terms
i=0#set counter to 0
if num <=0:
    print("Please enter valid positive no")
elif num ==1:
    print(n1)
else:
    print("Fibonnaci Series:")
    while i <num:
        print(n1,end=' ')
        next=n1+n2 #next term=addition of last 2 terms
        n1=n2 #2nd term becomes 1st
        n2=next #next term becomes 2nd term
        i=i+1