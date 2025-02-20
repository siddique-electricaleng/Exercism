"""
30. Field names with DictReader and DictWriter
31. Reading and writing multiple files
32. The csv DictWriter (coded inside medals_dict.py)
33. The zip function
34. Reading and writing to the same text file
35. Solution to parsing functions challenge
"""
import csv
import sys
import os
# 30) Field names with DictReader (he didn't show DictWriter yet)
""" 
import csv
import sys
dir_path = "." + sys.path[0].removeprefix('c:\\Users\\Acer\\Exercism')
country_filename = dir_path + '\\country_info.txt'
dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(country_filename, encoding='utf-8', newline='') as countries_file:
    # Get the column headings from the file and make it lowercase
    headings = countries_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    

    reader = csv.DictReader(countries_file, dialect = dialect, fieldnames=headings)

    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

user_test = input(
    "Enter the Country or 2 letter country code to see it's capital: ").casefold()
print(
    f"The capital of {countries[user_test]['country']} is {countries[user_test]['capital']}\r")
"""

# Reading and Writing multiple files at the same time - continue from 1.30
# Code obtained from their provided file: generate_medals_data.txt
""" 
dir_path = ".\\" + sys.path[0].strip('c:\\Users\\Abdul-Hamid\\Exercism')
ordering = ['Country', 'Gold', 'Silver', 'Bronze', 'Rank']
# Note the lack of 'Total' in `ordering`

with open((dir_path+'\OlympicMedals_2020.csv'), encoding='utf-8', newline='') as data, \
        open((dir_path + '\medals_dict.py'), 'w', encoding='utf-8') as output_file:
    # Write the first part of the code (excluding the actual data)
    print('import csv', file=output_file)
    print(file=output_file)
    print('medals_table = [', file=output_file)

    reader = csv.DictReader(data)
    # Read each row from the CSV file, as a dictionary,
    # and produce a new dictionary containing the key/value
    # pairs we want, in the order we want.
    for row_dict in reader:
        new_dict = {}
        # Only print the values for the keys we want
        # (in the order we want them).
        for key in ordering:
            value = row_dict[key]
            if value.isnumeric():
                value = int(value)
            new_dict[key.casefold()] = value

        # print the dictionary to the output file
        # (indented by 4 spaces, with a trailing comma).
        print(f'    {new_dict},', file=output_file)

    # All the data rows have been written, print the terminating ]
    print(']', file=output_file)
    print(file=output_file)  # and finish with a blank line.
"""

# 33. The zip function
# This is a list of tuples for song albums
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Imelda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]
# We want to use DictWriter to write this info into a csv file
keys = ['album', 'artist', 'year']
remove_str = os.path.expanduser("~") + "\\Exercism"
dir_path = ".\\" + sys.path[0].strip(remove_str)
file_path = dir_path + "\\albums.csv"
print(remove_str)
for row in albums:
    zip_object = zip(keys, row)
    # zip object is an iterable producing exactly a tuple with 2 elements.
    # Since there are 3 keys, therefore for each row there will be 3 such tuples containing the key and value pairs

    # We can pass this zip object which is an iterable into the dict() function to convert to a dictionary
    albums_dict = dict(zip_object)
    with open(file_path, 'w', encoding='utf-8', newline='') as output_album_file:
        writer = csv.DictWriter(output_album_file)
