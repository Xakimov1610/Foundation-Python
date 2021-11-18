nimadir = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count = 0
for i in nimadir:
    if isinstance(i, int):
        count += 1
print(count)