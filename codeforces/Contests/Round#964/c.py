#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, s, total = map(int, input().split())
        arr = []
        for i in range(n):
            a, b = map(int, input().split())
            arr.append((a, b))
        can = False

        if arr[0][0] >= s:
            print('YES')
            continue
        start = arr[0][1]
        for i in range(1, n):
            if arr[i][0] - start >= s:
                can = True
                break
            start = arr[i][1]
        if total - start >= s:
            can = True
        print('YES' if can else 'NO')
            

