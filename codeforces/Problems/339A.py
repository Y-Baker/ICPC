#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        l = list(map(int, input().split('+')))
        l.sort()
        print('+'.join(map(str, l)))

