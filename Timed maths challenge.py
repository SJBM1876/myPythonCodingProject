import random

OPERATORS = ["+", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 10

def create_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    print(expr)
    return expr

create_question()


