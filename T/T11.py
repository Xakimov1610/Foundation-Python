import Vars

ages = Vars.T11


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


result = filter(is_prime, ages)
print(list(result))
