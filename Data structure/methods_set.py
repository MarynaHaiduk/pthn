# Set is a collection which is unordered and unindexed. No duplicate members.
# The elements in the set are immutable but the set as a whole is mutable.
# Contain string, numbers, tuple.

# Create set
s = set("elements")  # {'m', 'e', 't', 'l', 'n', 's'} <class 'set'>
s = {'elements'}  # {'elements'} <class 'set'>
s = {1, 345.23, 345.23, (1, 754, 4.3, 4.3)}  # {345.23, 1, (1, 754, 4.3, 4.3)} <class 'set'>
# s = {['test', 1, (12, 23)]}  # TypeError: unhashable type: 'list'

# Set operations
s = {1, 2, 3, 4}
print(f"The set has {len(s)} elements.")

# Add to set
s.add('foo')  # add one element: {1, 2, 3, 4, 'foo'}
s.update(['bar', 'spam'])  # add list: {'foo', 1, 2, 3, 4, 'spam', 'bar'}
s.update({'test', 'easy'})  # add set: {'easy', 1, 2, 3, 4, 'spam', 'bar', 'test', 'foo'}
s.update((111, 222))  # add tuple: {1, 2, 3, 4, 'test', 111, 'easy', 'spam', 'foo', 222, 'bar'}

# Create set
s = set()  # create an empty set: set() <class 'set'>
s = {"one"}  # create set with one element: {'one'}
s = {}  # {} <class 'dict'>
s = set('one')  # create set from sequence, only for iterable: {'e', 'n', 'o'}
s = {i * 2 for i in range(5)}  # create set from sequence: {0, 2, 4, 6, 8}
# s = set(map(int, input().split()))
s = set(("a", "b", "c"))  # create set. Note: the double round-brackets!!!: {'a', 'b', 'c'}

# Set operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
print(len(s1))  # get the length of a set: 5
print(2 in s1)  # True/False if element in set: True
print(2 not in s1)  # True/False if element in set: False
for i in s1: print(i, end=" ")  # loop through the set: 1 2 3 4 5
print(s1 == s2)  # True/False if _all elements s1 in s2 and _all elements s2 in s1: False
# Sorting
print(tuple(sorted(s1)))  # sort a set, return a tuple: (1, 2, 3, 4, 5)

# Union
print(s1 | s2)  # new set with elements from both s1 and s2: {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2))  # same as s1 | s2: {1, 2, 3, 4, 5, 6, 7}
print({8}.union(enumerate("one")))  # {8, (1, 'n'), (2, 'e'), (0, 'o')}

# Intersection
print(s1 & s2)  # new set with elements common to s1 and s2: {4, 5}
print(s1.intersection(s2))  # same as s1 & s2: {4, 5}

# Difference
print(s1 - s2)  # new set with difference difference between two or more sets: {1, 2, 3}
print(s1.difference(s2))  # same as s1 - s2: {1, 2, 3}

# Not in both
print(s1 ^ s2)  # new set with elements from s1 or s2 (but not in both): {1, 2, 3, 6, 7}
print(s1.symmetric_difference(s2))  # same as s1 ^ s2: {1, 2, 3, 6, 7}

# Copy
print(s1.copy())  # return new set with a copy of s1: {1, 2, 3, 4, 5}

# Return True/False
print(s1 <= s2)  # True/False if s2 contains s1 or not: False
print(s1.issubset(s2))  # same as s1 <= s2: False

print(s1 >= s2)  # True/False if s1 contains s2 or not: False
print(s1.issuperset(s2))  # same as s1 >= s2: False

print(s1.isdisjoint(s2))  # True if no common elements: False

# Add: s1.update(s2), s1|s2, s1.union(s2)
s1.add(8)  # s1: {1, 2, 3, 4, 5, 8}
s1.update(s2)  # return set s1 with elements added from s2.
s1 |= s2  # same as s1.update(s2)
print(s1)  # s1: {1, 2, 3, 4, 5, 6, 7, 8}

# s1 will be equal intersection of 2 sets
s1.intersection_update(s2)  # return set s1 keeping only elements also found in s2
s1 &= s2  # same as s1.intersection_update(s2)
print(s1)  # s1: {4, 5, 6, 7}

# s1 will be equal _all elements from both without common elements
s1.symmetric_difference_update(s2)
s1 ^= s2  # return s1 with elements from s1 or s2 but not both
print(s1)  # s1: {4, 5, 6, 7}

# s1 will be equal s1 difference and s2 elements
s1.difference_update(s2)  # return set s1 after removing elements found in s2
s1 -= s2  # same as s1.difference_update(s2)
print(s1)  # set()

# Remove
s1 = {1, 2, 3, 4, 5}
s1.discard(1)  # Remove the specified item. If element not exist, will NOT raise an error.
print(s1)  # s1: {2, 3, 4, 5}
s1.remove(2)  # Remove the specified item. If element not exist, raise KeyError.
print(s1)  # s1: {3, 4, 5}
num = s1.pop()  # Remove and return an arbitrary element from s1. Raises KeyError if empty
print(num, s1)  # 3 {4, 5}
s1.clear()  # Removes _all the elements from the set
print(s1)  # s1: set()
del s1  # delete the set completely
