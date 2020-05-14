#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

'''mydic1={1:1**2,2:2**2,3:3**2} #Dictionary creation
print(mydic1)

print(mydic1.items())'''

def mydic():
    intdic=dict()
    intdic['1']=1**2 #key=value pairing
    intdic['2']=2**2
    intdic['3']=3**2
    return intdic

print("Dictionary \n",mydic())