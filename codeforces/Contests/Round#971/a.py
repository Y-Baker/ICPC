#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict, deque
from math import ceil

if __name__ == '__main__':
    t = 1
    t = int(input())


    for _ in range(t):
        n, k = map(int, input().split())
        end = n + k - 1
        l = 1
        r = n - 1

        def getValue(x):
            sum1 = (k + x - 1) * (k + x) // 2 - (k - 1) * k // 2
            sum2 = (end) * (end + 1) // 2 - (k + x - 1) * (k + x) // 2
            return abs(sum1 - sum2)
        
        ans = -1
        found = False
        while l < r:
            mid = l + (r - l) // 2
            x = getValue(mid)
            before = getValue(mid - 1)
            after = getValue(mid + 1)
            if x < after and x < before:
                ans = x
                found = True
                break
            elif x > after:
                l = mid + 1
            else:
                r = mid
        if found:
            print(ans)
        else:
            print(getValue(l))
