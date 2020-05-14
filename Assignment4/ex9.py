#Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
list1=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda x:x**2,list1))#map(function,iterator)..so lambda for function
print("Old List:\n",list1)
print("New List:\n",result)