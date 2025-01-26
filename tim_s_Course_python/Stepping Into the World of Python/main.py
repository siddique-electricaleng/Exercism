"""
Topics Covered from Tim's:
1.	The Escape Character
2.	More on Escape Characters
3.	Python is a Strongly Typed Language

4.	Expressions
5.	Operator Precedence

6.	Negative Indexing in Strings
7.	Slicing with Negative Numbers
8.	Using a Step in a Slice
9.	Slicing Backwards
10.	Challenge Solution and Slicing Idioms

11.	String Replacement Fields
12.	String Formatting
13.	Python 2 String Interpolation
"""

# 1. Escape Character - \n, \t, \', \", """ """, \\
# new line
splitString = "This string has been\nsplit over\nseveral\nlines"
# print(splitString)
# tab
tabbedString = "1\t2\t3\t4\t5"
# print(tabbedString)
# single quote
# print('The pet shop owner said "No, no he\'s uh,... he\'s resting".')
# double quote
# print("The pet shop owner said \"No, no, he's uh,...he's resting\".")
# Triple quotes - split into several lines

anotherSplitString = """This string has been
split over\
 several
lines
"""

# print(anotherSplitString)

# 6 - Negative Indexing in Strings
parrot = "Norwegian Blue"
"""
print(parrot[-4:-2])
print(parrot[-4:12])
"""

# 8 - Slicing using step
number = "9,223;372:036 854,775;807"
separators = number[1::4] #Start from 1th element first comma and take every 4 comma or separator
# print (separators)
values = "".join(chr if chr not in separators else "" for chr in number)
# print([int(val) for val in values])

# 9 Slicing backwards

letters = "abcdefghijklmnopqrstuvxyz"

backwards = letters[25:0:-1]
print(backwards)
backwards_full = letters[25::-1]
# print(backwards_full)
backwards_full_alt = letters[::-1]
# print(backwards_full_alt)

# print(letters[16:13:-1])
# print(letters[4::-1])
# print(letters[:25-8:-1])

# 11. String Replacement Fields
"""
3 ways:
1. Coerce number into string using str()
2. Use {index} + .format(values)
3. fstrings: f"{VARIABLE_NAME_OR_VAL}"
"""
age = 25
# print("My age is "+ str(age) + " years")
# Examples with {index} + .format(values)
# print("My age is {0} years".format(age))
# print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
#       .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# 12. String Formatting
for i in range(1, 13):
    # print ("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))
    pass

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))

print("Checking python's precision")
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))