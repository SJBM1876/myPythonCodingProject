name = input("What's your name: ")
print("Welcome", name, "to the greatest adventure ever known.")

scenario = input("You wake up in unfamiliar surroundings. There is a path to your left and another to your right. Type right or left to choose the direction you will take: ").lower()

if scenario == "left":
    scenario = input("In front of you there is a river. You need to get to the other side. Type swim to swim across the river or walk to walk around it: ").lower()
    if scenario == "swim":
        print("Game Over! You were eaten by a crocodile.")
    elif scenario == "walk":
        print("Game over! You tripped into the river and were eaten by a crocodile.")
    else:
        print("Game over! You failed to meke the correct choice.")

elif scenario == "right":
    scenario = input("In front of you is a lake. You need to get to the other side. Type swim to swim across the lake or walk to walk around the lake: ").lower()
    if scenario == "swim":
        print("Game Over! You were eaten by an alligator.")
    elif scenario == "walk":
        print("Game over! You tripped into the river and were eaten by an alligator.")
else: 
    print("You failed to choose left or right. Your adventure is over.")