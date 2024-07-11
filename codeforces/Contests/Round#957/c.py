#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, m, k = map(int, input().split())
        arr = [0] * n
        i = n
        idx = 0
        while i >= k:
            arr[idx] = i
            i -= 1
            idx += 1
        i = m
        idx = n - 1
        while i > 0:
            arr[idx] = i
            i -= 1
            idx -= 1

        x = m + 1
        for i in range(n):
            if arr[i] == 0:
                arr[i] = x
                x += 1
        print(*arr)