"""
Suppose you are given a price list of some products. Write a simple python program that can print
the prices along with product number and the total price of all products.

"""

price = [500, 550, 880, 1600, 1500]
total = 0
for i in range(len(price)):
    print("Product_no: ", (i+1), "  ", "Price: ", price[i])
    total = total + price[i]

print("The total price of all products: ", total)
