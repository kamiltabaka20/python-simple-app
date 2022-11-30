from random import randint


def check_name(name):
    if name.isalpha():
        print("Hello {0}!".format(name.capitalize()))
        return name.capitalize()

    print("Incorrect name - note, that provided name can only contains letters with no numbers or special characters.")
    return False


def draw_number():
    number = randint(1, 100)
    print("Today, your lucky number is {0}!".format(number))
    return number
