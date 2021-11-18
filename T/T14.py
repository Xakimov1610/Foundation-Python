a = 60
b = 5
if a < b:
    a, b = b, a

def func(a1, b1):
    trash = []
    c = list(range(b1, a1))
    [trash.append(i) for i in range(2, b1) if i**2 in c]
    return trash if trash else None


print(func(a, b))



