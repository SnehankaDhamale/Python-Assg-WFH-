#Write a Python program to print all natural numbers from 1 to n.
def find_nat(n):
 for i in range(1,n+1): #loop iterate from 1 to n+1
  print(i,end=' ') #print all nos and end=' ' gives ' ' between output

no=int(input("Enter the number:"))
find_nat(no)