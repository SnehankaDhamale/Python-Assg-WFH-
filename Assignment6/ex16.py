#Write a Python program to enter a number and print its reverse.

no = int(input("Enter the number:"))
rev = 0
while no > 0:
    rem = no % 10
    rev = (rev * 10) + rem
    no = no // 10

print("Reverse number:", rev)


