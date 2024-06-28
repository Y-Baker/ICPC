#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(1 if a >= b else 0)

