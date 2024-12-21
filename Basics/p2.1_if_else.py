"""
write a simple python program that can take an input from a user, and it can check whether
it is even or odd.
"""

num = input("Enter a number: ")
num = int(num)

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")