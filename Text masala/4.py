def find_len_less_5(file_name):
    file = open(file_name)
    txt = file.read()
    file.close()
    words = txt.strip().split()
    count = 0

    for i in words:
        if len(i) < 5:
            count += 1
    return count


print(find_len_less_5("text.txt"))

