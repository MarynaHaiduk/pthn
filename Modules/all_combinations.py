import itertools


def all_combinations(arr1, arr2):
    return list(itertools.product(arr1, arr2))


print(all_combinations([1, 2, 3], [3, 4, 7]))
# [(1, 3), (1, 4), (1, 7), (2, 3), (2, 4), (2, 7), (3, 3), (3, 4), (3, 7)]
