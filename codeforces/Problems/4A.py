#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        if n % 2 == 0 and n != 2:
            print('YES')
        else:
            print('NO')
