import random
import time

OPERATORS = ["+", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 10
TOTAL_QUESTIONS = 5

def create_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong =0
input("Press enter to start.")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_QUESTIONS):
    expr, answer = create_question()
    while True:
        guess = input("Question #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("----------------------")
print("Well done! You finished in ", total_time, " seconds.")




