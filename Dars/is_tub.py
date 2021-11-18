def is_tub(son):
    for i in range(2, son):
        if son % i == 0:
            return False
    return True

print(is_tub(5))
