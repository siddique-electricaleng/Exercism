"""
30. Field names with DictReader and DictWriter
31. Reading and writing multiple files
32. The csv DictWriter
33. The zip function
34. Reading and writing to the same text file
35. Solution to parsing functions challenge
"""
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

