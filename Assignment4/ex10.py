#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

list1=[1,2,3,4,5,6,7,8,9,10]
print("Original List",list1)
even_list=list(filter(lambda x:x%2==0,list1))
print("Even nos:",even_list)
square_list=list(map(lambda x:x**2,even_list))
print("Square of Even nos:",square_list)