# Wap to find out total no of lines total no of words total no of characters in file

#fname="abc.txt"
fname=input("Enter the filename:")
num_lines = 0
num_words = 0
num_chars = 0

with open (fname,'r') as f: #open file in read mode
    for lines in f: #loop
        words = lines.split() #split the string into list i.e default seperator is whitespace
        num_lines += 1
        num_words += len(words)
        num_chars += len(lines)

print("Total no of Lines:",num_lines,"\nTotal words:",num_words,"\nTotal no of Characters:",num_chars)