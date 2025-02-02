""" 
HiLo - using binary search
"""

low = 1
high = 10
print("Please guess a number between 1 and 1000")
input("Press Enter to Start")
guesses = 1
num_guesses = 0
while True:
    # Guesses is basically the midpoint between two integer numbers
    guesses = low + (high-low) // 2
    num_guesses += 1
    print("#{}".format(num_guesses), end=" ")
    print("{0} - {1}".format(low, high))
    high_low = input("My guess is {}. Should I guess higher(H) or lower(L) or am I correct(C)?"
                     .format(guesses)).strip().upper()
    if high_low == 'H':
        low = guesses + 1
    elif high_low == 'L':
        high = guesses - 1
    elif high_low == 'C':
        print("I got it in {0} guesses. It is {1}".format(
            num_guesses, guesses))
        break
    elif num_guesses > 10:
        print("You exceeded {} guesses. Check Algorithm".format(num_guesses))
        break
    else:
        print("Please enter H, L or C")


# else in a loop
""" 
numbers = [1, 45, 32, 12, 60]
for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
 """
