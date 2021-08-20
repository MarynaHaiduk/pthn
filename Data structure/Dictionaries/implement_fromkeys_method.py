def fromkeys_method(*args, value=None):
    d = {}
    for i in args:
        d[i] = value
    return d


print(fromkeys_method(1, 2, 3))  # {1: None, 2: None, 3: None}
