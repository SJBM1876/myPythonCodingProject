import random

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

for i in range(TOTAL_QUESTIONS):
    expr, answer = create_question()
    guess = input("Question #" + str(i + 1) + ": " + expr + " = ")
    print(guess)



