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

answer = input("Who were the first side to win the world cup twice? ")
if answer.lower() == "Italy".lower():
    print("GOAL!")
    score += 1
else:
    print("SAVED!")

answer = input("Who was the top goalscorer in the 1986 world cup? ")
if answer.lower() == "Gary Lineker".lower():
    print("GOAL!")
    score += 1
else:
    print("SAVED!")

answer = input("Who won the golden glove award in the 2022 world cup? ")
if answer.lower() == "Emi Martinez".lower():
    print("GOAL!")
    score += 1
else:
    print("SAVED!")



print("Congratulations! You got " + str(score) + " correct.")
print("You scored " + str((score/5) * 100) + "%")
if score == 5:
    print("You are a World Cup winner!")







