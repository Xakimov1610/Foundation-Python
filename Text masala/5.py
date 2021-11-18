def is_word_capitalize(file_name):
    file = open(file_name)
    txt = file.read()
    file.close()
    words = txt.strip().split()
    count = 0

    for i in words:
        if i[0].isupper():
            count += 1

    return count


print(is_word_capitalize("text.txt"))
