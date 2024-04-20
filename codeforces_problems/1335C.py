#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sett = set()
        freq = [0 for _ in range(n + 1)]

        for ele in arr:
            sett.add(ele)
            freq[ele] += 1

        maxx = max(freq)
        distinct = len(sett)
        if distinct == maxx:
            print(maxx - 1)
        elif distinct < maxx:
            print(distinct)
        else:
            print(maxx)
