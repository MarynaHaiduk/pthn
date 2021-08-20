def interval_overlap(l1, l2):
    return max(l1[0], l2[0]) <= min(l1[1], l2[1])


print(interval_overlap([1, 7], [2, 10]))  # True
print(interval_overlap([1, 3], [4, 10]))  # False
