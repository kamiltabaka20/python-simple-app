def check_name(name):
    if name.isalpha():
        print("Hello {0}!".format(name.capitalize()))
        return name.capitalize()

    print("Incorrect name - note, that provided name can only contains letters with no numbers or special characters.")
    return False
