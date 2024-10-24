#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        rowA = (a - 1) // 3
        rowB = (b - 1) // 3
        a = a % 3 - 1
        b = b % 3 - 1
        if a == -1:
            a = 2
        if b == -1:
            b = 2

        if abs(a - b) == 1 and rowA == rowB:
            print('Yes')
        else:
            print('No')
