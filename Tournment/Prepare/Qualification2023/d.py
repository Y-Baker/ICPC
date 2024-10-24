#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        if n == 63:
            print('=')
        else:
            print('<' if n < 63 else '>')
