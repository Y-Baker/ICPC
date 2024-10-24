#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())
        if x > y:
            print(y, x)
        else:
            print(x, y)

