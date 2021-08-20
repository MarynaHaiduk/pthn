# Solution 1
# def length_without_spaces(s):
#     return len(s) - s.count(" ")


# Solution 2
def length_without_spaces(s):
    return len(s.replace(" ", ""))


s = "  Some  string... "
print(length_without_spaces(s))
