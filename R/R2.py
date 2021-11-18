arr1= [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]

list1 = []

list1.extend(arr1[0])
print(list1)
list1.remove(list1[-1])
print(list1)
list1.extend(arr1[1])
print(list1)