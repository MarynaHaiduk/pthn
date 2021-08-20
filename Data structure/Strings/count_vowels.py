# solution 1
def count_vowels1(s):
    count = 0
    for i in s.lower():
        if i in "aeoiu":
            count += 1
    return count


# solution 2
def count_vowels2(s):
    vowels = "aeiuoAEIOU"
    return sum(i in vowels for i in s)


# solution 3 with lambda function
func = lambda s, vowels: sum(i in vowels for i in s)
print(func("maa rybai sghA", "aeiuoAEIOU"))

print(count_vowels1("maa rybai sghA"))  # 5
print(count_vowels2("maa rybai sghA"))  # 5
