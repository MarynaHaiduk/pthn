def consonants(s):
    for i in s:
        if i not in "aioueAIOUE":
            print(i, end=" ")


s = 'abcdefghijklmnopqrstuvwxyz'
consonants(s)
