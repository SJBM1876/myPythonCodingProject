def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Type a number to find out if it's odd or even: "))
result = even_or_odd(number)
print(f"{number} is {result}")

