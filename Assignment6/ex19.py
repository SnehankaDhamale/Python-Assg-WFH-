#Write a Python program to find power of a each number using for loop
no=int(input("Enter the number:"))
exponent=int(input("Enter value for exponent:"))
power=1
for i in range(1,exponent+1):
    power=power*no #calculate power by multiplying with same no upto expo
print("The",no,"power",exponent,"is:",power)