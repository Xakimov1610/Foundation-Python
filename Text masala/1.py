def t_in_line(file_name):
    file = open(file_name)
    txt = file.read()
    file.close()
    words = txt.strip().split('\n')
    count = 0

    for i in words:
        if 'T' not in i:
            count += 1
    return count


print(t_in_line("text.txt"))

