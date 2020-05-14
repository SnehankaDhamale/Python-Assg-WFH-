# Write a Python program to find first and last digit of a number.
no=int(input("Enter the no:"))
first_digit = no
while first_digit >=10: #condition to find first single digit
    first_digit=first_digit//10 
last_digit = no % 10 #return last digit
print("First Digit of no:",first_digit)
print("Last Digit of no:",last_digit)

