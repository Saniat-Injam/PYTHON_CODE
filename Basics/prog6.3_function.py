# Write a simple python program using function that can sum up two numbers.

def caculate_sum(a, b):
    sum = 0
    sum = a + b
    return sum

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

result = caculate_sum(x, y)
print("The result is: ", result)
