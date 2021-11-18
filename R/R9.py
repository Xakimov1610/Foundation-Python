arr = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
new = []
for i in arr:
    i = list(i)
    i.reverse()
    new.append(i)

new.sort()
arr.clear()
for i in new:
    i.reverse()
    arr.append(i)
print(arr)


# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

