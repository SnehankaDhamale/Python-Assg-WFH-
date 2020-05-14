# Write a Python program to find sum of first and last digit of a number.

no=int(input("Enter the number:"))
first_digit=no
while first_digit >=10: #retuen first digit
    first_digit=first_digit//10

last_digit = no % 10 #return last digit
sum=first_digit + last_digit #sum of digits
print("First Digit=",first_digit,"\nLast Digit=",last_digit)
print("Sum:",sum)