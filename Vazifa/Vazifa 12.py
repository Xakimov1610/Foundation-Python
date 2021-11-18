# find max num
trash = input("3 ta son kiriting: ").split()
son1 = int(trash[0])
son2 = int(trash[1])
son3 = int(trash[2])

if son1 < son2:
    son1 = son2
if son1 < son3:
    son1 = son3

print(son3)
