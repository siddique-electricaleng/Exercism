""" 
HiLo - using binary search
"""

low = 1
high = 1000
print("Please guess a number between 1 and 1000")
input("Press Enter to Start")
guesses = 1
num_guesses = 1
while (low != high):
    # Guesses is basically the midpoint between two integer numbers
    guesses = low + (high-low) // 2
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
    num_guesses += 1
else:
    print("Low == High reached.")
    print("I got it in {} guesses. It is {}".format(num_guesses, guesses))

# else in a loop
""" 
numbers = [1, 45, 32, 12, 60]
for number in nSumbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
 """
