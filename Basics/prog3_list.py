fruits = ["Mango", "Banana", "Lichi", "Apple", "Pine apple"]
print(fruits)

item1 = fruits[0]
print(item1)
item2 = fruits[1]
print(item2)
item3 = fruits[2]
print(item3)

print(fruits[3])
print(fruits[4])

fruits[0] = "Ripe Mango"
print(fruits)

print(fruits[0:2])
print(fruits[-1])

fruits.append("Lemon")
print(fruits)

fruits.insert(1, "Green Mango")
print(fruits)

groceries = ["Rice", "Egg", "Oil", "Potato", "Sugar"]

all_items = fruits + groceries
print(all_items)

item_count = len(all_items)
print(item_count)


var = "Lemon" in all_items
print(var)
print("Lemon" in all_items)
print("Guava" in all_items)


