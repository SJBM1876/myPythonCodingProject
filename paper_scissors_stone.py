import random

player_wins = 0
computer_wins = 0

options = ["paper", "scissors", "stone"]

while True:
    player_input = input("Type paper, scissors or stone or Q to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in options:
        continue

    random_number = random.randint(0, 2)
    # paper: 0, scissors: 1, stone: 3
    computer_pick = options[random_number]
    print("The computer picked " + str(computer_pick) + ".")

    if player_input == "stone" and computer_pick == "scissors":
        print("You won!")
        player_wins += 1
        continue
        

    elif player_input == "scissors" and computer_pick == "paper":
        print("You won!")
        player_wins += 1
        continue

    elif player_input == "paper" and computer_pick == "stone":
        print("You won!")
        player_wins += 1
        continue

    elif player_input == "stone" and computer_pick == "stone":
        print("It's a draw!")
        player_wins += 1
        continue

    elif player_input == "paper" and computer_pick == "paper":
        print("It's a draw!")
        player_wins += 1
        continue

    elif player_input == "scissors" and computer_pick == "scissors":
        print("It's a draw!")
        player_wins += 1
        continue

    else:
        print("You lose!")
        computer_wins += 1

print("You won " + str(player_wins) + " times.")
print("The computer won " + str(computer_wins) + " times")


print("Goodbye. Thanks for playing")


