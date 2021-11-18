def is_how_many(file_name):
    file = open(file_name)
    txt = file.read()
    file.close()

    return txt.count("is")


print(is_how_many("text.txt"))