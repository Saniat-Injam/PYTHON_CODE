# Function is a block of code that performs special task

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]


def calculate_sum(list):
    sum = 0 
    for i in list:  
        sum = sum + i
    return sum

odd_sum = calculate_sum(list1)
print("The summation of all odd elements are: ", odd_sum)

even_sum = calculate_sum(list2)
print("The summation of all even elemets are: ", even_sum)