arr1 = [11, 22, 33, 44, 55, 66, 77]
arr2 = [21, 18, 43, 40, 59, 31, 80]

[print(arr1[i]) if arr1[i] > arr2[i] else print(arr2[i]) for i in range(len(arr1))]
