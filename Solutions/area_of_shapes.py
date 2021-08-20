from math import sin


def area_of_square(a):
    return a * a


def area_of_rectangle(a, b):
    return a * b


def area_of_parallelogramm1(a, h):
    # Solution 1. The square of parallelogram through side and height.
    return a * h


def area_of_parallelogramm2(a, b, anger):
    # Solution 2. The square of parallelogram through sides and angles.
    return a * b * sin(anger)


def area_of_parallelogramm3(d1, d2, anger):
    # Solution 3. The square of parallelogram.
    return 1 / 2 * d1 * d2 * sin(anger)
