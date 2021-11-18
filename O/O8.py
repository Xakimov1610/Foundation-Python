list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
trash = []
trash.extend([list1[i] + list2[i] for i in range(len(list2))])
print(trash)