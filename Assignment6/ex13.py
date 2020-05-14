#Write a Python program to swap first and last digits of a number

'''num = int(input("Enter a number: "))
num1 = num
# first we will count the digits
count = 0
while num1 > 0:
    count += 1
    num1 //= 10

# #print(count)
# then we will use count-1 as power of 10
# and find 1st and last nos.

power = 10 ** (count - 1)
first = num // power
last = num % 10

# #print(first, last, power)
# then we find the number without 1st and last nos.

num3 = num % (first * power)

# #print(num3)

num3 //= 10

# #print(num3)
# now we finally find the swapped output

swap = (last * power) + (num3 * 10) + first
print(swap)
'''


no=input("Enter the number:")
list1=list(no) #convert string into list
size=len(list1) #calculate list length
temp=list1[0] #swapping
list1[0]=list1[size-1]
list1[size-1]=temp
print("Before swapping:",no)
no1=" "
for i in list1: #convert list into string
    no1+=i
print("After swapping first and last digit:",no1)

#print("After swapping:",no1.join(list1)) convert list into string bt with space

