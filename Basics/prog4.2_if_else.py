""""
You are given 3 lists of continent. Each continent contains some countries. Write a simple
python program using if else and in keyword to find out whether a specific country exists
in those lists or not.
"""


asia = ["Bangladesh", "India", "Pakistan", "Nepal", "Sri Lanka"]
europe = ["England", "France", "Italy", "Germany", "Austria"]
north_america = ["USA", "Canada", "Mexico", "Cuba", "Costa Rica"]

country = input("Enter a country: ")

if country in asia:
    print("The country is a Asian country")
elif country in europe:
    print("The country is a European country")
elif country in north_america:
    print("The country is a North American country")
else:
    print("We don't know")


