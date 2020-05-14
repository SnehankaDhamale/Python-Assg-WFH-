#Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

'''lis=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
for i in lis:
    if i%2==0:
     even_list.append(i)
print(even_list)'''

list1=[1,2,3,4,5,6,7,8,9,10]
condition=lambda x:x%2==0 #for filter need lambda ..i.e condition
even_list=list(filter(condition,list1)) #filter(function,iterator)
print(even_list)