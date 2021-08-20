def sum_arrays_numbers(arr1, arr2):
    tmp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            tmp[i][j] = arr1[i][j] + arr2[i][j]
    return tmp


arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(sum_arrays_numbers(arr1, arr2))
# [[11, 13, 15], [17, 19, 21], [23, 25, 27]]
