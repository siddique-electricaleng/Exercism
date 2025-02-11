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
# 24) Reading a CSV file
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
""" 
input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:

    # Reading 3 lines for a sample:
    samples = ""
    for i in range(3):
        samples += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(samples)

    # Move file pointer to beginning of file using seek() method
    countries_data.seek(0)

    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)
 """
# 27) CSV Dialect - seeing what is inside the Dialect Object
# Using the previous code
""" 
print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace'
              ]

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
 """
# 28) Writing a CSV File
""" 
cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1],
    ["Rye", 422, 2, 31.4, 18.2, 21.2],
    ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
    ["Triticale", 338, 1.81, 36.6, 19, 0.9],
    ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
]

column_headings = ["Cereal", "Calories",
                   "Fat", "Protein", "Fibre", "Vitamin E"]

output_filename = 'my_cereals.csv'

with open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
    # Create the writer object
    writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
    # Write the column heading first
    writer.writerow(column_headings)
    # Use the writer object to write each row 1 at a time
    writer.writerows(cereals)
"""
# 29) The csv DictReader
