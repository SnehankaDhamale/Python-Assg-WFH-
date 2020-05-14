#Write a Python program to print all ASCII character with their values
for i in range(1,255): #ascii range is 1-254
    ch=chr(i) #typecast int to char
    print(i,"=>",ch)