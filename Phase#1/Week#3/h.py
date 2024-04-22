#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    n = int(input())
    mapp = {}

    for _ in range(n):
        k, v = map(int, input().split())
        mapp[k] = v

    mapp = sorted(mapp.items(), key=lambda x: x[0])
    l = 0
    r = 0
    start = mapp[0][0]

    while l < n:
        tmp = l + 1
        if tmp >= n:
            print(start, mapp[r][1])
            break

        if mapp[tmp][0] > mapp[r][1]:
            print(start, mapp[r][1])
            start = mapp[tmp][0]
            l = r = tmp
        else:
            l = tmp
            if mapp[r][1] < mapp[tmp][1]:
                r = tmp
