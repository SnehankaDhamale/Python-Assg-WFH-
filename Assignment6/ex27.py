#Write a Python program to print all Armstrong numbers between 1 to n
no=int(input("Enter the no:"))
print("Total armstrong nos lies between 1 to",no)
for i in range(1,no+1):
    power=len(str(no))#calculate power
    sum=0
    temp=i
    while temp >0:
        digit=temp %10
        sum=sum+digit **power #calculate the sum of no with resp power
        temp=temp//10
        if i==sum: #check amstrong no's condition
            print(i,end=' ')