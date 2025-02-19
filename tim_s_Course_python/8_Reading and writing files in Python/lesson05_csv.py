"""
30. Field names with DictReader and DictWriter
31. Reading and writing multiple files
32. The csv DictWriter
33. The zip function
34. Reading and writing to the same text file
35. Solution to parsing functions challenge
"""

import csv
import sys
dir_path = "." + sys.path[0].removeprefix('c:\\Users\\Abdul-Hamid\\Exercism')
country_filename = dir_path + '\\country_info.txt'
dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(country_filename, encoding='utf-8', newline='') as countries_file:
    # Get the column headings from the 
    reader = csv.DictReader(countries_file, dialect = dialect)

    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

user_test = input(
    "Enter the Country or 2 letter coutnry code to see it's capital: ").casefold()
print(
    f"The capital of {countries[user_test]['Country']} is {countries[user_test]['Capital']}\r")
 