a = 1
print(a)  # a=1

a, b = 2, 3
print(a, b)  # a=2, b=3

[a, b] = [5, 6]
print(a, b)  # a=5, b=6

a, b, c, d = "text"
print(a, b, c, d)  # a=t, b=e, c=x, d=t

a, *b = "text"
print(a, b)  # a=t, b=['e', 'x', 't']

a = b = 0
print(a, b)  # a=0, b=0
