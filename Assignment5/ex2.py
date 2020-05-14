#Wap to convert the content of files in reverse order.

fname=input("Enter the filename:") # reverse file linewise
for line in reversed(list(open(fname))): #inbuild reversed function
    print(line.rstrip()) #rstrip remove trailing character and return copy of string

