#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        cnt = 0
        while n > 0:
            cnt += n
            n = n // 2
        print(cnt)

