#Find count of each and every word in file

fname=input("Enter the filename:")
num_lines = 0
num_words = 0


with open (fname,'r') as f: #open file in read mode
    for lines in f: #loop
        words = lines.split() #split the string into list i.e default seperator is whitespace
        num_lines += 1
        num_words += len(words)

print("\nTotal words:",num_words)