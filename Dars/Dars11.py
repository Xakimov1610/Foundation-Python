numbers = [1, 2, 3, 4, 5]
numbers1 = [5, 4, 3, 2, 1]

result = map(lambda x, y: x + y, numbers, numbers1)
print(list(result))