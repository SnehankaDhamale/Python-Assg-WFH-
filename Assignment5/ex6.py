#Wap to accept username and password from user and validate from file.

#username = "sneha"
#password = "Sneha12"
file = open(r"C:\Users\ADMIN\PycharmProjects\Assignment5\sneha.txt", 'r')

data = file.read()
words = data.split() #split() convert file into list
username = input("Enter the username:")
if username ==  words[0]: #compare 1st element of list ..index0
    password = input("Enter the Password:")
    if password == words[1] :#compare 2nd element of list ..index1
        print("Login Successfull.........\nWelcome",username)
    else:
        print("Wrong Password")
else:
    print("Wrong Username")