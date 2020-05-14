#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
numbers=range(1,21)
list1=list(filter(lambda x:x%2==0,numbers))

print("Even nos between 1-20:",list1)