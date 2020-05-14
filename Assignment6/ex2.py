#Write a Python program to print all natural numbers in reverse (from n to 1).

def rev_nat(n):
    for i in range(n,0,-1): #loop iterate from n to 0 and decrement bt 1
        print (i,end=' ') # end= ' ' prints 'space' after char

no=int(input("Enter the no:"))
rev_nat(no)