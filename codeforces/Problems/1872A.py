#!/usr/bin/python3

from math import ceil
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())
        median = (a + b) / 2
        needed = abs(median - a)
        cnt = ceil(needed / c)
        print(cnt)
