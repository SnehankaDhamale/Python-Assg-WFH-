#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

def cal_len(str1,str2):
    no1=len(str1)
    no2=len(str2)
    if no1 == no2:
        print("Both strings are equal", str1, str2)
    else:
     if no1 > no2:
        print(str1," string1 has maximum lenght")
    #if no2>no1 :
     else :
        print(str2, " string2 has maximum lenght")


str1=input("Enter the first string:")
str2=input("Enter the second string:")
cal_len(str1,str2)