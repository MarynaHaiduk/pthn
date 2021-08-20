def check_input(s):
    if s.isdigit():
        return "You entered the number(s)."
    elif s.isalpha():
        return "You entered the letter(s)."
    else:
        return s


s = input()
print(check_input(s))
