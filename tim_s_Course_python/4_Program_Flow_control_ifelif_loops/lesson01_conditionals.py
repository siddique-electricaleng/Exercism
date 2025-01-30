"""
1. Intro to Blocks & Statements (not useful)
2. Using a debugger in IntelliJ or Pycharm [watched the one for vscode's built-in Run & Debug]
3. If, elif, else in debugger.(not useful - but watched still. Can do with VSCode)
4. Adding a Second Guess (did it but very silly)
5. Challenge Solution (silly)
6. Simplify Chained Comparison (silly - already did with exercism but did here anyways)
7. Truthy Values (skipped)
8. In & not in (skipped)
9. if challenge
"""

# Using a debugger in VSCode (not IntelliJ or PyCharm):
answer = 5
print("Please enter a number between 1 and 10: ")
guess = int(input())
if guess < answer:
    print("Please guess higher: ")
    # 4. Adding a Second Guess
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you didn't guess correctly")
elif guess > answer:
    print("Please guess lower: ")
    # 4. Adding a Second Guess
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you didn't guess correctly")
else:
    print("You got it first time")
print('-'*40)
# 6. Simplify Chained Comparisons
name = input("Enter your name: ")
age = int(input("How old are you {0}: ".format(name)))
if age >= 16 and age <= 65:
    print("Have a good day at work")
# Chaining the above:
if 16<= age <= 65:
    print("Have a good day at work")

#  9: if challenge
yourName = input("Enter your name: ")
yourAge = int(input("Please enter your age {0}: ".format(yourName)))

if 18<= yourAge < 31:
    print("Welcome to the (18-30) Holiday club, {0}".format(yourName))
else:
    print("Sorry, {0} you are not in our age range".format(yourName))