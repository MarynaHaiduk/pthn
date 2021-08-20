def remove_numeric_digits(s):
    letters = ""
    for i in s:
        if not i.isdigit():
            letters += i
    return letters


print(remove_numeric_digits("akshat123garg"))  # akshatgarg
