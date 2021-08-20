def change_tuple(t, idx, value):
    tmp = list(t)
    tmp[idx] = value
    return tuple(tmp)


print(change_tuple((1, 2, 3), 0, 5))  # (5, 2, 3)
