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
with open('Jabberwocky.txt', 'r') as jabbo:
    lines = jabbo.readlines()

# print(lines)
print(lines[-1:])

for line in reversed(lines):
    print(line.rstrip())
