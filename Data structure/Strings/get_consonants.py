def get_consonants(word):
    vowels = "AEOUIaeoui"
    consonants = ""

    for i in word:
        if i not in vowels:
            consonants += i
    return consonants


print(get_consonants("consonant"))  # cnsnnt
