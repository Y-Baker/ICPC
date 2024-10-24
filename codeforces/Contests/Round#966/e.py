#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict
from math import ceil

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, m, k = map(int, input().split())
        num = int(input())
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        grid = [[0 for i in range(m)] for j in range(n)]

        counts = []

        for i in range(n):
            for j in range(m):
                if i + k <= n and j + k <= m:
                    for x in range(i, i + k):
                        for y in range(j, j + k):
                            grid[x][y] += 1

        for i in range(n):
            for j in range(m):
                print(grid[i][j], end=' ')
                grid[i][j] = 'X'
            print()

        for i in range(0, n // 2 if n % 2 == 0 else n // 2 + 1):
            start = i + 1
            if start > k:
                start = k
            p = start
            for j in range(0, m // 2 if m % 2 == 0 else m // 2 + 1):
                grid[i][j] = start
                grid[i][m - j - 1] = start
                grid[n - i - 1][j] = start
                grid[n - i - 1][m - j - 1] = start
                start += p
                if start > k * p:
                    start = k * p

        for i in range(n):
            for j in range(m):
                counts.append(grid[i][j])

        counts.sort(reverse=True)
        sum = 0
        for idx, i in enumerate(arr):
            sum += counts[idx] * i
        print(sum)
