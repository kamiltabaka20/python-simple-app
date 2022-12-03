from number_drawing import draw_number
from name_checker import check_name
from file_creator import write_to_a_file
from db_connector import *


# Checking user's name from input
user_name = check_name(input("What's your name?\n"))
while not user_name:
    user_name = check_name(input("Try again, please.\n"))

# Drawing a lucky number for the user
user_number = draw_number()

# Sending taken data to a .txt file
write_to_a_file(user_name + ' ' + str(user_number))

# Sending taken data to database
db_data(user_name, user_number)
