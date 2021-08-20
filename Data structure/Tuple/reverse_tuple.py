# Solution 1
def reverse_tuple1(t):
    return t[::-1]


# Solution 2
def reverse_tuple2(t):
    new_tuple = ()
    for i in reversed(t):
        new_tuple += i,
    return new_tuple


t = ('k', 'e', 'f', 'd', 'a', 'z')
print(reverse_tuple1(t))
print(reverse_tuple1(t))
# ('z', 'a', 'd', 'f', 'e', 'k')
