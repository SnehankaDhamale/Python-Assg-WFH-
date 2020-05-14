#Write a Python program to print all even numbers between 1 to 100.

numbers =range(1,101)
even_list=list(filter(lambda x:x%2==0,numbers))

print("Even numbers from 1 to 100:\n",even_list)
