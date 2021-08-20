def print_integers(i, n):
    if i == n:
        return n
    else:
        print(i, end=" ")
        return print_integers(i + 1, n)


print(print_integers(0, 5))  # 0 1 2 3 4 5
