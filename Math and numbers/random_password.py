import random, string


def random_password(length):
    char = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(char) for i in range(0, length))


print(random_password(10))
