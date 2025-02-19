"""
Topics covered in lesson 1:
5. Reading from a text file
6. Opening a file using 'with'
7. read readline and readlines
8. strip lstrip and rstrip
9. removeprefix and removesuffix in Python
10. Parsing data in a text file
11. Working with text data
12. Solution to capital city challenge
"""

# 5. Reading from a text file : Jabberwocky.txt

#  Open file in read mode
"""
jabber = open('Jabberwocky.txt', 'r')

for line in jabber:
    print(line, end='')
"""
# Close the file
# jabber.close()

# 6. Opening  a file using 'with' block
"""
with open('Jabberwocky.txt', 'r') as jaber:
    for line in jaber:
        print(line.rstrip())
"""
# 7. read, readline and readlines

# readlines()
"""
with open('Jabberwocky.txt', 'r') as jabbo:
    lines = jabbo.readlines()

# print(lines)
print(lines[-1:])

for line in reversed(lines):
    print(line.rstrip())
 """
# read()
"""
with open("Jabberwocky.txt", 'r') as jabo:
    text = jabo.read()

print(text)
 """

# 8) strip lstrip and rstrip
"""
filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first_line = poem.readline().rstrip()

print("Original line:\n", first_line)

chars_to_remove = "'Twasebv"
processed_text = first_line.strip(chars_to_remove)
print(processed_text)
"""

# 9 removePrefix() and removeSuffix():
"""
file_name = "Jabberwocky.txt"
with open(file_name) as jabber:
    first_line = jabber.readline().rstrip()

print("Original Line:\n", first_line)

twas_removed = first_line.removeprefix("'Twas")
print(twas_removed)
toves_removed = first_line.removesuffix("toves")
print(toves_removed)
"""
# 10 Parsing data in a text file & 11) Working with text data
file_name = "country_info.txt"
countries = dict()

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
        # print(countries)

# 12 - Solution to capital city - my solution was actually quite good imo
input_country = input("Get Capital of the Country:").casefold()
while input_country not in countries.keys():
    if input_country == "quit":
        print(f"You could not find your country, you {
              input_country.upper()}!!!!")
        break
    print("The country does not exist.Please retype.")
    input_country = input("Retype Country to get Capital:").casefold()

else:
    print(countries[input_country]["capital"])
