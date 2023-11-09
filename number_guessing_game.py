import random

num = str(random.randrange(1000, 9999)) # Converted form integer to string

n = input("Guess a number between 1000 and 9999: ") # Input is now a string

if n == num:
    print("Congratulations! You guessed the number first time.")
else:
    guess_number = 1 # guess_number changed from 0 to 1

    while n != num:
        guess_number += 1
        count = 0

        n = str(n)

        num = str(num)

        correct = ['X'] * 4

        for i in range(0, 4):
            if n[i] == num[i]:
                count += 1
                correct[i] = n[i]
# Removed else statment after for loop. Added elif and new else statement
        if count == 0:
            print("No numbers match.")
        elif count == 1:
            print("Not quite. You got 1 number correct.")
        elif count == 2:
            print("Not quite. You got 2 numbers correct.")
        elif count == 3:
            print("Not quite. You got 3 numbers correct.")
        else:
            print("Congratulations! You guessed correct.")
            print("You guessed the number in", guess_number, "attempt/s")
            break

        n = input("Try again: ") # Moved from before the if statement

        if n == num:
            print("Congratulations! You guessed correct.")
            print("You guessed the number in ", guess_number, " attempts.")
            break