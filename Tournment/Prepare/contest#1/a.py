#!/usr/bin/python3

from math import comb
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(comb(a, 2) + comb(b, 2))

