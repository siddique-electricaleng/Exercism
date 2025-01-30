"""
In this lesson we are covering:
10. Stepping through a for loop (checking if something is a number using .isnumeric() )
11. For loops extracting values from user input
12. More about ranges
13. Continue
14. Break
15. Initializing variables and None
16. Break in while loop
"""

# 10. Stepping through a for loop

# number = input("Please enter a series of numbers using any separators you like: ")
number = "3, 2, 4"
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

# 14. break and 15. Initializing variables and None

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None


#  this below demonstrates break, however python is a very rich language and we can write the below much better
""" 
for index in range(len(item_to_find)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
 """
#  Writing the above in a much better way:
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))


# 16. Break in a while loop
available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ").casefold()
    if chosen_exit == "quit":
        print("Game Over")
        break

print("Aren't you glad you got out of there")