#!/usr/bin/python3
# from itertools import permutations, combinations
from collections import defaultdict
if __name__ == '__main__':
    t = 1
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        s = list(input())
        prefix = [0] * (n + 1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + arr[i-1]
        l = 0
        r = n - 1
        summ = 0
        while l < r:
            while l < n and s[l] != 'L':
                l += 1
            while r >= 0 and s[r] != 'R':
                r -= 1
            if l < r:
                summ += prefix[r+1] - prefix[l]
                l += 1
                r -= 1
        print(summ)