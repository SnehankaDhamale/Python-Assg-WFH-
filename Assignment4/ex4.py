#Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

def cal_even(x):

    if x%2==0:
        print(x,":It is an even number")
    else:
        print(x,"It is an odd number")

no=input("Enter the no:")
cal_even(int(no))