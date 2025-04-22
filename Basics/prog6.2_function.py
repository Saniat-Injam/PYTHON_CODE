# Function is a block of code that performs special task.

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = [10, 20, 30, 40, 50]

def calculate_sum(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

sum_of_odds = calculate_sum(list1)
print("Summation of all odd elements: ", sum_of_odds)

sum_of_evens = calculate_sum(list2)
print("Summation of all even elements: ", sum_of_evens)

sum_of_decades = calculate_sum(list3)
print("Summation of all decades: ", sum_of_decades)