n = int(input("List uzunligini kiriting: "))
ls = []

for i in range(n):
    ls.append(int(input()))

def son_kv(lst):
    new = []
    for i in lst:
        new.append(i*i)
    return new


print(son_kv(ls))
