#Write a Python program to find frequency of each digit in a given integer
from collections import Counter

num = int(input("Enter the number:"))
print("Frequency of each digit in number:")
frequency = Counter(str(abs(num)))
print(frequency)


