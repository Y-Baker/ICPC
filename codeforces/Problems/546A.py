#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        k, n, w = map(int, input().split())
        total = w * (w + 1) // 2 * k
        print(max(0, total - n))
