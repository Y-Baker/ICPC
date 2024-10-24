#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, m, a, b = map(int, input().split())
        cnt = 0
        while n > m:
            half = n // 2
            cost = (n - half) * b
            if cost > a and half >= m:
                n = half
                cnt += a
            else:
                cnt += b * (n - m)
                break
        print(cnt)
            

