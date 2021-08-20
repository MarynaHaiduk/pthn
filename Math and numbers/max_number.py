def max_number(*arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num


print(max_number(1, 2, 3, 4, 5))
