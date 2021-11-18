ages = [5, 12, 1, 17, 18, 24, 32, 19, 0, 21]


def is_tub(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


result = filter(is_tub, ages)

print(list(result))
