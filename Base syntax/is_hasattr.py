arr = [1, 2, 3, 4, 5]

if hasattr(arr, '__iter__'):
    print("Iterated sequence.")
else:
    print("No iterated sequence.")
