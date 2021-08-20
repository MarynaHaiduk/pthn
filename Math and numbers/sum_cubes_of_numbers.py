def sum_cubes_of_numbers(number):
    cubes = [i ** 3 for i in range(0, number)]
    print(cubes)
    return sum(cubes)


print(sum_cubes_of_numbers(int(input())))
