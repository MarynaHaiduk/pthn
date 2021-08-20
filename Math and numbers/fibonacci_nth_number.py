def fibonacci_nth_number(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_nth_number(n - 1) + fibonacci_nth_number(n - 2)


# Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21..
print(fibonacci_nth_number(5))
