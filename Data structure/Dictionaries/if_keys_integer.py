def if_keys_integer(d):
    for k in d:
        if type(k) == int:
            return True
    return False


d1 = {"a": 3, "b": 1, "c": 2}
print(if_keys_integer(d1))  # False

d2 = {1: 3, 2: 4}
print(if_keys_integer(d2))  # True
