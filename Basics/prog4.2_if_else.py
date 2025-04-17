""""
You are given 3 lists of continent. Each list contains some countries. Write a simple
python program using if else and in keyword to find whether a specific country that 
entered by user exists in those lists or not.

"""


asia = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan"]
europe = ["England", "France", "Italy", "Germany", "Austria"]
north_america = ["USA", "Canada", "Mexico", "Cuba", "Costa Rica"]

country = input("Enter a country: ")

if country in asia:
    print("The country is a Asian country", country)
elif country in europe:
    print("The country is a European country", country)
elif country in north_america:
    print("The country is a North American country", country)
else:
    print("We don't know")


