# O(n ** 2) when always picks greatest or smallest element as pivot.
# O(n log(n)) when always picks the middle element as pivot.
# Pick first/last/random/median element as pivot.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        mid = []

        for i in arr:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                mid.append(i)

        return quick_sort(left) + mid + quick_sort(right)


print(quick_sort([3, 2, 1]))  # [1, 2, 3]
