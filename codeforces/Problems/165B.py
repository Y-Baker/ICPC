#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        l = 0
        r = n
        def can(m):
            x = m
            cnt = m
            while x > 0:
                x = x // k
                cnt += x
            return cnt >= n



        while l <= r:
            m = l + (r - l) // 2
            if can(m):
                r = m - 1
            else:
                l = m + 1

        print(l)

