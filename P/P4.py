# Input:        [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
# Output:     [2, 5, 1, 4, 3, 6, 8, 7, 9]

Input = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
zet = []

for i in Input:
    if Input.count(i) == 1 or i not in zet:
        zet.append(i)

Input = zet
print(Input)