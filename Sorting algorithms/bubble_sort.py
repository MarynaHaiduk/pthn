# Time complexity: O(n) when array is already sorted.
# Worst and average case time complexity: O(n ** 2) when array is reverse sorted.
# Auxiliary Space: O(1).


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swap = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    return arr


print(bubble_sort([5, 9, 1, 2, 4, 8, 6, 3, 7]))
