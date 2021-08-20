#!/usr/bin/python

def oddNumbers(l, r):
    arr = []
    for i in range(l, r + 1):
        if i % 2 != 0:
            arr.append(i)
    return arr


if __name__ == '__main__':
    l = int(input().strip())
    r = int(input().strip())
    res = oddNumbers(l, r)
    print(res)
