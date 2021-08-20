def is_palindrome(word):
    return word.lower() == word.lower()[::-1]


print(is_palindrome('word'))  # False
print(is_palindrome('ttt'))  # True