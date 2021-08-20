#!/usr/bin/python

def get_duplicates(arr1, arr2):
    return set(arr1) & set(arr2)


if __name__ == "__main__":
    arr1 = input().split()
    arr2 = input().split()
    print(get_duplicates(arr1, arr2))
