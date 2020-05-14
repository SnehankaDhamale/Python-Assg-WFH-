# Wap to convert each n every word in upper case in file

fname=input("Enter the filename:")
for line in open(fname):
    print(line.upper(),end='') #upper() coverts letters to uppercase