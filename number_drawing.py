from random import randint


def draw_number():
    number = randint(1, 100)
    print("Your today's lucky number is {0}!".format(number))
    return number
