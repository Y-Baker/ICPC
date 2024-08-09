#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = input()
        lower = 0
        upper = 0
        for i in s:
            if i.islower():
                lower += 1
            else:
                upper += 1
        if lower >= upper:
            print(s.lower())
        else:
            print(s.upper())

