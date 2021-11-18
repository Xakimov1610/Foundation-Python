def how_many_words(file_name):
    file = open(file_name)
    txt = file.read()
    file.close()

    words = txt.strip().split()
    return len(words)


print(how_many_words("text.txt"))
