def alternating_haracters(s):
    arr = []

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            arr.append(s[i])
        else:
            continue

    return len(arr)


print(alternating_haracters('AAAA'))  # 3
print(alternating_haracters('BBBBB'))  # 4
print(alternating_haracters('ABABABAB'))  # 0
print(alternating_haracters('BABABA'))  # 0
print(alternating_haracters('AAABBB'))  # 4
