list1 = [19, 23, 32, -4, 5, 16, 27, 8]
list2 = []
list3 = []
count = 0


for i in list1:
    if i % 2 == 0:
        count += 1
        list2.append(i)


list3.extend([i // 2 for i in list2])
print(count, list3, end=' ')




# for i in list2:
#     list3.append(i // 2)
#
# print(count, list3, end=' ')
















