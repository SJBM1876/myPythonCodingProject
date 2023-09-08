from random import *

randint(0, 20)

random_number = int(randint(0, 20))

print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Guess a number betweem 0 and 20: "))

    if user_guess == random_number:
        print("Congratulations! Great Guess.")
        break

    elif user_guess < random_number:
        print("That's too low. Have another guess: ")

    else:
        print("That's too high. Have another go: ")


    

    
        

    
    


