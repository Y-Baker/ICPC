#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # n_diff = 4
    # t = int(input())

    for _ in range(t):
        n = int(input()) # number of eggs
        colors = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

        res = ''
        start = n // 7
        for i in range(start):
            res += ''.join(colors)

        if n % 7 == 1:
            res += 'G'
        if n % 7 == 2:
            res += 'GB'
        if n % 7 == 3:
            res += 'YGB'
        if n % 7 == 4:
            res += 'OYGB'
        if n % 7 == 5:
            res += 'OYGBI'
        if n % 7 == 6:
            res += 'OYGBIV'

        print(res)
