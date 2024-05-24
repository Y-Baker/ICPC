#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, k, sum = map(int, input().split())
        lower = k * (k + 1) // 2
        upper = k * (2 * n - k + 1) // 2
        # upper = n * (n + 1) // 2 - (n - k) * (n - k + 1) // 2
        print('YES' if sum >= lower and sum <= upper else 'NO')
