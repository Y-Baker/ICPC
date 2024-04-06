#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        a, b, n, s = map(int, input().split())
        needed = 0
        r = s // n
        r = min(r, a)
        if r > a:
            print('NO')
        else:
            needed = s - r * n
            if needed > b:
                print('NO')
            else:
                print('YES')

