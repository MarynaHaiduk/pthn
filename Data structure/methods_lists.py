arr = [1, 2, 3]

print(arr[0])
print(arr[1:2])
print(arr.index(1))  # or ValueError
print(arr.count(1))
print(arr + arr)  # concatenate two lists
print(arr * 4)  # repeat
print(len(arr))  # 10
print()

# Change lists elements
arr[0] = 5
print(arr)
arr.extend([7, 8])
print(arr)
arr.append(8)  # adding an item to the list
print(arr)
arr.insert(1, 'one')  # add elements
print(arr)
print()

# Input and Output the elements of the list with even indices
print(arr[::2])
print()

# Reverse the list
print(arr[::-1])
print()

# Input and Output the minimum and maximum value of the list
print(max(arr), min(arr))
print()

# Copy
arr2 = arr.copy()
print("Copy a list:", arr2)
print()

# Add items
arr.insert(1, 55)
print(arr)  # [0, 55, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print()

# Delete items
arr.remove('one')
print(arr)
arr.pop()
print(arr)
# arr.clear()
del arr[0]
print(arr)  # [55, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# remove all list items which index is a multiple of 3
del arr[::3]
print()

# Sorting
arr.sort()
print(arr)  # [0, 1, 1, 1, 2, 2, 3, 3, 4, 55]
arr.sort(reverse=True)
print(arr)  # [55, 4, 3, 3, 2, 2, 1, 1, 1, 0]
arr.sort(key=lambda x: x)
print(arr)  # [0, 1, 1, 1, 2, 2, 3, 3, 4, 55]
arr2 = sorted(arr, reverse=True)
print(arr2)
arr2 = sorted(arr)
print(arr2)
arr.reverse()
print("Reverse order a list:", arr)
print()