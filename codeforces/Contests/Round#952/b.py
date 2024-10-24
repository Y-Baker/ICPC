#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        cnt = 0
        maxx = -1
        re = 2
        for x in range(2, n+1):
            curr = x
            p = 1
            while curr <= n:
                curr *= p
                p += 1
                cnt += 1
            if cnt >= maxx:
                re = x
                maxx = cnt
            cnt = 0
        print(re)
        