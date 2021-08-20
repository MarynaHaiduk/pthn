import math


def sum_factorials(numbers):
    return sum([math.factorial(n) for n in numbers])


print(sum_factorials([1, 2, 3]))
