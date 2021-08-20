def reversed_digits(n):
    if n < 10:
        return n
    else:
        print(n % 10)
        return reversed_digits(n // 10)


print(reversed_digits(12345))
