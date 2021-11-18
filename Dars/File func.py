


def is_file_empty(file_name):
    file_name = open(file_name)
    file = file_name.read().strip()
    file_name.close()

    return bool(file)


print(is_file_empty("login.txt"))





