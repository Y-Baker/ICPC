#!/usr/bin/python3

from math import ceil
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(ceil((a-1) / (b-1)))
