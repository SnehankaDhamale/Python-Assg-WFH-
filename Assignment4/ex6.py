#Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
'''range(20)
print(list(range(20)))

def fun(): #function which print sq of 1-20
    for i in range(1,21):
     print(i,i**2)

fun()'''

def fundic():
    numbers=range(1,21)
    my_dic={}
    for i in numbers:
     my_dic[i]=i**2
    print("Dictionary:\n",my_dic)
fundic()

