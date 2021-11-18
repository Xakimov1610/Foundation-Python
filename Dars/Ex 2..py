list1 = [2, 1, -4, -9, 0, -5, 8, 3]
list2 = [-4, 0, 2, 9, 6, 1]

# for i in list1:
#     if i not in list2:
#         print(i)
# for j in list2:
#     if j not in list1:
#         print(j)

for i in list1:
    for j in list2:
        if j not in list1 and i not in list2:
            print(f"list1 {i}")
            print(f"list2 {j}")
