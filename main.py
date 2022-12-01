from number_drawing import draw_number
from name_checker import check_name


# Checking user's name from input
user_name = check_name(input("What's your name?\n"))
while not user_name:
    user_name = check_name(input("Try again, please.\n"))

# Drawing a lucky number for the user
user_number = draw_number()
