# Write a simple python program using function that can sum up two numbers

def calculate_sum(a, b):
    sum = a + b
    return sum

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = calculate_sum(x, y)
print("The calculated sum is: ", result)

