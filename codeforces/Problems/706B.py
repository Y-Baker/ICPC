#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        q = int(input())

        a.sort()

        for _ in range(q):
            x = int(input())
            from bisect import bisect_right
            print(bisect_right(a, x))
