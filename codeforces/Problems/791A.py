#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        years = 0
        while a <= b:
            a *= 3
            b *= 2
            years += 1
        print(years)

