#!/usr/bin/python

if __name__ == '__main__':
    number = int(input())
    country = set()
    i = 0

    while i < number:
        country.add(input())
        i += 1

    print(len(country))
