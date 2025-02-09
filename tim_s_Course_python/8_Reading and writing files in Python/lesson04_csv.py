"""
264 - 23) The CSV format - no coding
265 - 24) Reading in a CSV file
266 - 25) Quoting in a CSV file
267 - 26) Sniffer and Dialect
268 - 27) CSV Dialect
269 - 28) Writing in a CSV file
270 - 29) The csv DictReader
271 - 30) Solution to DictReader Challenge
"""
import csv
# 24) Reading in a CSV file
""" 
csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    # Read the headers only using readline()
    headers = csv_file.readline().strip('\n').split(',')
    # print(f"Column headers: {headers}")
    # Read the remaining lines by iterating over the readers object
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
 """
# 25) Quoting in a CSV file (using cereals_grains.csv)
""" 
cereals_filename = 'cereal_grains.csv'
with open(cereals_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
 """

# 26) Sniffer and Dialect
input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as csv_file:
    country_reader = csv.reader(csv_file, delimiter='|')
    for row in country_reader:
        print(row)
