#!/usr/bin/python

if __name__ == '__main__':
    M = int(input())
    s1 = set(map(int, input().split()))

    N = int(input())
    s2 = set(map(int, input().split()))

    print(len(s1.union(s2)))

"""
Sample Input: 
2   2 4
3   2 3 4
"""
