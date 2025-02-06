"""
20) Serializing data using JSON
21) Limitations of JSON
22) Practical application parsing JSON data
23) Practical application parsing JSON data from the internet
"""
import json
import urllib.request
# 20) Serializing data using JSON
""" 
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]
# Writing the data
with open('test.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

# Reading the data back from the test.json file
with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])
"""
# 21) Practical application parsing JSON data
""" 
json_data_source = 'temperature_anomaly.json'
with open(json_data_source, 'r', encoding='utf-8') as json_temp_data:
    anomalies = json.load(json_temp_data)

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f"{year}...{value:6.2f}")
"""
# 22) Practical application parsing JSON data from the internet
url_data_source_json = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/tavg/land_ocean/1/12/1850-2024/data.json'

# download json data from the internet
with urllib.request.urlopen(url_data_source_json) as json_stream:
    # returns a string containing the JSON.
    data = json_stream.read().decode('UTF-8')
    anomalies = json.loads(data)

print(type(anomalies))
#  printing the year....value

for year in anomalies['data']:
    print(f"{year}...{anomalies['data'][str(year)]['anomaly']}")
