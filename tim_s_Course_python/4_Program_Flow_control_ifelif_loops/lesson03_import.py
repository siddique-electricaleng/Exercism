"""
17. Random Module and Import
18. Challenge Solution
"""
import random
# We are changing the guessing game from lesson02_import.py
highest = 12
answer = random.randint(1,highest)
print("Please guess a number between 1 and {}: ".format(highest)) #TODO: Remove after testing
guess = int(input())

while not(guess == answer):
    if guess == 0:
        print("Game Over")
        break
    elif guess < answer:
        print("Guess Higher: ")
        guess = int(input())
    elif guess > answer:
        print("Guess Lower: ")
        guess = int(input())

if guess != 0:
    print("Well done, you guessed it")