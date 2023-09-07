print("Welcome to the FIFA World Cup Quiz.")
print("Test your knowledge on the FIFA Word Cup from the inaugral 1930 world cup in Uruguay to the 2022 world cup in Qatar.")
playing = input("Are you ready to play?: ")

if playing.lower() != "yes":
    quit()

print("Let's kick off")
score = 0

answer = input("Who won the very first world cup in 1930? ")
if answer.lower() == "Uruguay".lower():
    print("GOAL!")
    score += 1
else:
    print("SAVED!")


answer = input("Who were the first European to win the world cup? ")
if answer.lower() == "Italy".lower():
    print("GOAL!")
    score += 1
else:
    print("SAVED!")

print("Congratulations! You got " + str(score) + " questions correct.")
print("You scored " + str((score/2) * 100) + "%")







