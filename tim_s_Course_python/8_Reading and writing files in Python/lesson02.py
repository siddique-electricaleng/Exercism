"""
13) Dictionary values with multiple keys - done
14) Printing data to a text file - done
15) Writing data to a text file - tbc
16) File modes
18) Unicode in Python
19) File encodings
"""

# 13 - dictionary with multiple keys - marked where we can
file_name = "country_info.txt"
countries = dict()
""" 
with open(file_name) as country_file:
    # Just read the first line to throw it away
    # we can also use next(country_file) <- to run the first iteration and skip over to the next
    country_file.readline()

    for row in country_file:
        data = row.rstrip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data

        # Creating a dictionary to store the values
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        countries[country.casefold()] = country_dict
        # modification in lesson 13
        countries[code.casefold()] = country_dict


input_country = input(
    "Enter Country Name or 2 letter Code to get capital:").casefold()
while input_country not in countries.keys():
    if input_country == "quit":
        print(f"You could not find your country, you {
              input_country.upper()}!!!!")
        break
    print("The country does not exist.Please retype.")
    input_country = input(
        "Re-enter Country Name or 2 letter Code to get capital:").casefold()
else:
    country_capital = countries[input_country]["capital"]
    if not country_capital:
        print(f"{countries[input_country]
              ['name']} does not have a capital")
    else:
        print(country_capital)
 """

# 14) Printing data to a text file
""" 
# Data to be stored
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]
#  Storing inside the file
plants_filename = "flowers_print.txt"

with open(plants_filename, 'w') as plants:
    for plant in data:
        print(plant, file=plants)

#  Reading the stored data from the file
new_list = []
with open(plants_filename) as plants:
    for plant in plants:
        new_list.append(plant.rstrip())
print(new_list)
 """
# 15) Writing data to a text file - another way to store data to the text file
# Data to be stored

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]
#  Storing inside the file
plants_filename = "flowers_write.txt"

with open(plants_filename, 'w') as plants:
    for plant in data:
        plants.write(plant)

# Understanding the __str__ method in python:
# print(data)
# string_representation = data.__str__()
# print(string_representation)

# storing integer using .write():
file_name_int = 'store_integers.txt'
with open(file_name_int, 'w') as integers:
    for i in range(10):
        integers.write(i.__str__())


# 18) Unicode in Python
