def print_nums():
    for i in range(0, 4):
        print(i)


def print_nums2():
    for i in range(0, 4):
        print(i, end=" ")


def print_nums3():
    i = 0
    while i < 4:
        print(i)
        i += 1


print_nums()
print_nums2()
print_nums3()
