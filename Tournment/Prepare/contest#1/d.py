#!/usr/bin/python3

from collections import defaultdict
from math import comb

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1

        combs = defaultdict(int)
        sum = 0
        for k, v in freq.items():
            x = comb(v, 2)
            sum += x
            combs[k] = x

        # print(freq, combs)
        for i in range(n):
            tmp = arr[i]
            print(sum - combs[tmp] + comb(freq[tmp] - 1, 2))
