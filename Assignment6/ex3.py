#Write a Python program to print all alphabets from a to z.

def print_alpha():

    print("Alphabets in lowercase:")
    for i in range(97,123):   #ascii value a=97,z=122    here n+1 so 123
        print(chr(i),end=' ')  #typecast int (i) to char

    print("\n\nAlphabets in uppercase:")
    for i in range(65,91):   #ascii value A=65,Z=90    here n+1 so 91
        print(chr(i),end=' ')  #typecast int (i) to char

print_alpha()
