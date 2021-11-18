son = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

result = 1, 1

for i in son:
    if son.count(i) > result[1]:
        result = i, son.count(i)
print(f"{result[0]} --> {result[1]} marta")