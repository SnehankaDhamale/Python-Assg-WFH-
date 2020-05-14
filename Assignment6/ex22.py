#Write a Python program to find HCF (GCD) of two numbers

'''a=no1
b=no2
while no2 !=0:
    temp=no2
    no2=no1%no2
    no1=temp
hcf=no1
print("Highest common factor(HCF) of",a,"and",b,"is:",hcf) '''
no1=float(input("Enter the first number:"))
no2=float(input("Enter the second number:"))

i=1 #starts from 1
while i<= no1 and i<=no2 :  #check all nos which are less than both no
    if no1%i == 0 and no2%i ==0: #check condition for both no
        hcf=i
    i=i+1

print("Highest common factor(HCF) of",no1,"and",no2,"is:",hcf)
