list1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
int_arr = []
int_arr.extend([i for i in list1 if isinstance(i, int)])
int_arr.sort()
print(int_arr[-1])

