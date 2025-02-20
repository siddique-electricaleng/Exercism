"""
30. Field names with DictReader and DictWriter
31. Reading and writing multiple files
32. The csv DictWriter (coded inside medals_dict.py)
33. The zip function
34. Reading and writing to the same text file
35. Solution to parsing functions challenge
36. The recordinvoice function
37. Using the recordinvoice function
38. seek & tell
39. Improving the recordinvoice function
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
""" 
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Imelda May", 2011),
    ("Ride the Lightning", "Metallica", 1984)
]
# We want to use DictWriter to write this info into a csv file
keys = ['album', 'artist', 'year']

remove_str = os.path.expanduser("~") + "\\Exercism"
dir_path = ".\\" + sys.path[0].strip(remove_str)
file_path = dir_path + "\\albums.csv"


with open(file_path, 'w', encoding='utf-8', newline='') as output_album_file:
    writer = csv.DictWriter(output_album_file, fieldnames=keys)
    writer.writeheader()

    # Convert the 2 lists into a list of tuples using zip function
    for row in albums:
        zip_object = zip(keys, row)
        # convert zip object or the (key,value) tuples into a dictionary for DictWriter to write to a csv
        albums_dict = dict(zip_object)
        # Since we are inside the loop. We must write each row individually to the csv and not altogether
        writer.writerow(albums_dict)
"""
# 34. Reading and writing to the same text file  & parsing 
# Code already provided semi-completed.
# We did the code for parse_invoice_number & next_invoice_number functions

import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    # TODO1: Completed
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    return tuple(map(int, invoice_number.split('-')))


def next_invoice_number(invoice_number: str) -> str:
    # TODO2: Ongoing
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    year, prev_inv_num = parse_invoice_number(invoice_number)
    # return f"{get_year()}-{str(1 if (year!= get_year()) else (prev_inv_num + 1)).rjust(4,'0')}"
    return f"{get_year()}-{1 if (year!= get_year()) else (prev_inv_num + 1):04d}"

def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float) -> None:
    # TODO3: Future videos
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    """
    # read last line only
    last_row = ''
    for line in invoice_file:
        print(line) #TODO4: Delete after testing
        last_row = line
    if last_row:
        invoice_num, _, _ = last_row.split('\t')
        # TODO5: Need to finish this video as well as using the recordinvoice function
        


# Test code:
current_year = get_year()
test_data = [
    ('2019-0005', (2019, 5), f'{current_year}-0001'),
    (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
    (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
    (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
]

for test_string, result, next_number in test_data:
    parts = parse_invoice_number(test_string)
    if parts == result:
        print(f'{test_string} parsed successfully')
    else:
        print(f'{test_string} failed to parse. Expected {result} got {parts}')

    new_number = next_invoice_number(test_string)
    if next_number == new_number:
        print(f'New number {new_number} generated correctly for {test_string}')
    else:
        print(f'New number {new_number} is not correct for {test_string}')

    print('-' * 80)

