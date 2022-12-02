import uuid


# Output file related functions.
def create_name():
    name = uuid.uuid4()
    return name


def create_file():
    file = open(str(create_name()) + ".txt", "a")
    return file


def write_to_a_file(arg):
    file = create_file()
    file.write(arg)
    file.close()
    return file
