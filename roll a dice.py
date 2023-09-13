import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

def main():
    print("Beat your friend by rolling a higher score!")
    player1_name = input("Enter the name of player 1: ")
    player2_name = input("Enter the name of player 2: ")

    while True:
        input(f"{player1_name}, press enter to roll the dice.")
        player1_roll = roll()
        print(f"{player1_name} rolled a {player1_roll}")

        input(f"{player2_name}, press enter to roll the dice.")
        player2_roll = roll()
        print(f"{player2_name} rolled a {player2_roll}")

        if player1_roll > player2_roll:
            print(f"{player1_name} is the winner!")
              
        elif player1_roll < player2_roll:
            print(f"[player2_name] is the winner!")

        else:
            print("It's a draw!")
    
        play_again = input("Do you want to play again?: (yes/no)").strip().lower()
        if play_again != "yes":
            break

    print("Thanks for playing.")

if __name__ == "__main__":
    main()

    
    