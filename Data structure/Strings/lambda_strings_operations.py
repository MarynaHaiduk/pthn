def lambda_strings(s1, s2):
    string_length = lambda s1: len(s1)
    print("String length: ", string_length(s1))

    string_concatenation = lambda s1, s2: s1 + s2
    print("Concatenation strings: ", string_concatenation(s1, s2))

    count_words = lambda s1: len(s1.split(" "))
    print("The word count: ", count_words(s1))

    first_word = lambda s1: s1.strip().split(" ")[0]
    print("First word: ", first_word(s1))

    is_palindrom = lambda s1: True if s1.lower() == s1.lower()[::-1] else False
    print("Is the word palindrome?", is_palindrom(s1))

    count_vowels = lambda s1, vowels="aeiuo": sum(s1.count(i) for i in vowels)
    print("Vowels count: ", count_vowels(s1))


lambda_strings("abba", "qqq")
