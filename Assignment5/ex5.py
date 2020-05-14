#Wap to find out count of all the python files in any specific directory and subdirectory

import os #provide fun for interacting with OS
import glob#used to retrive files/pathnames matching a specified pattern

path=r"C:\Users\ADMIN\PycharmProjects\Assignment5" #r -rawstring so \ not consider escape character
g = glob.glob('*') #it displays files in current directory bt shows given path
for f in g:
    print(os.path.join(path, f))


print("\n---------- Current Directory Status ------------")
print ("Total no of files in current directory:",
       len([name for name in os.listdir('.') if os.path.isfile(name)])) # listdir() returns list of file in directory ..
                                                                        # if not specify dir name bydefault current directory
                                                                        #os.path.isfile() check whether specified path is an existing regular file or not

print ("Total no of subdirectory in current directory:",
       len([dir1 for dir1 in os.listdir('.') if os.path.isdir(dir1)]))
































