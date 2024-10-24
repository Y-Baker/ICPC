#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())
        print('+' if a + b == c else '-')

