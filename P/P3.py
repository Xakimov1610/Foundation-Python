arr = [2, 1, -4, -9, 0, -5, 3, 8]
num = 0


for i in range(len(arr)):
    if num < arr[i]:

        num = arr[i]

print(num)