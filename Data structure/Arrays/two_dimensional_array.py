from array import *


# In 2D-array the data is referred by two indices instead of one.
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# access to elements
print("First element:", arr[0])
print("First subarray element:", arr[0][0])

# insert/update
arr.insert(1, [10, 11, 12])
print("Insert an item:", arr)

arr[0][0] = 5
arr[1] = [12, 11, 10]
print("Updated array:", arr)

# delete
del arr[0]
print("Delete an item:", arr)

# print all array items
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
