#!/usr/bin/python3
from math import gcd

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        arr1.sort()

        for i in range(m):
            min_val = min(arr1)
            min_idx = arr1.index(min_val)
            arr1[min_idx] = arr2[i]

        print(sum(arr1))
        