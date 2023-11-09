import random

num = random.randrange(1000, 9999)

n = int(input("Guess a number between 1000 and 9999: "))

if (n == num):
    print("Congratulations! You guessed the number first time.")

else:
    guess_number = 0

while (n != num):
    guess_number += 1

    count = 0

    n = str(n)

    num = str(num)

    correct = ['X']*4

    for i in range(0, 4):

     if(n[i] == num[i]):

        count += 1

        correct[i] = n[i]
     else:
        continue

    print("Not quite. You got ", count, "correct.")

    print('\n')
    print('\n')
    n = int(input("Try again: "))

    if (count == 0):
        print("No numbers match.")

        n = int(input("Try again: "))

    elif n == num:
        guess_number += 1
        print("Congratulations! You guessed correct.")
        print ("You guessed th number in ", guess_number, "attempt/s")