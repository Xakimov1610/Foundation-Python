list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

a = 0

for i in list1:
    a += i
for i in list2:
    a += i
print(a / (len(list1) + len(list2)))
