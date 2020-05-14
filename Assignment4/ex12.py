#Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

'''numbers=range(1,20) #calculate perfect sqr from given range
for i in numbers:
    if(i**(.5)==int(i**(.5))):
        print(i)'''

numbers=range(1,21)
sqr_list=list(map(lambda x:x**2,numbers))
print("Original List:",list(numbers))
print("square list:",sqr_list)