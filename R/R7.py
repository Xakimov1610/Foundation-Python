list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new = []

for i in list1:
    if i:
        new.append(i)
print(new)
