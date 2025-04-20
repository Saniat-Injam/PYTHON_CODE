price_list = [100, 200, 300, 400, 500]

price = int(input("Enter your price: "))

for i in price_list:
    if i == price:
        print("The value is found in the list")
        break
    else:
        print("The value isn't found in the list")

        



"""
When you use break statement you just came out of the program, it didnt go through the entire list.
This is very usefil when you are doing real time programming. Suppose you have a list which has 
let's say 10k items. It will waste some CPU cycles it will be overburden on computer for the 
work that's gonna give noting

"""


