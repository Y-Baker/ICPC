#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        k = int(input())
        n = k * 3
        l = 1
        r = n
        print(k // 2 if k % 2 == 0 else (k + 1) // 2)
        while l < r:
            print(l, r)
            l += 3
            r -= 3
