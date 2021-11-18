list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
lsit2 = ["h", "i", "k"]
for i in lsit2:
    list1[2][1][2].append(i)

print(list1)