def longest_prefix(strs):
    # get one from the shortest words
    shortest_word = sorted(strs, key=lambda x: len(x))[0]

    # get maximum prefix length
    prefix_length = len(shortest_word)

    while prefix_length:
        # check if all chars the shortest word in other words
        common_prefix = all(word[:prefix_length] == shortest_word[:prefix_length] for word in strs)
        if common_prefix == True:
            return prefix_length
        else:
            prefix_length -= 1

    # if not found the output is ""
    return ""


print(longest_prefix(["cat", "care", "car"]))  # 2
print(longest_prefix(["zineone", "shine", "zoo"]))  # ""
print(longest_prefix(["zineone", "zhine", "zoo"]))  # 1
print(longest_prefix([""]))  # ""
