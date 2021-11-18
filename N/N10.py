str1 = input("Enter for 1-string: ")
str2 = input("Enter for 2-string: ")

new_arr = []
for i in str1:
    for j in str2:
        if i.strip() == j and j not in new_arr:
            new_arr.append(j)
            break

print(new_arr)