#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        while k > 0:
            if n % 10 == 0:
                n //= 10
            else:
                n -= 1
            k -= 1
        print(n)