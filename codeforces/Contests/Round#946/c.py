#!/usr/bin/python3

from collections import defaultdict
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        ab = defaultdict(int)
        bc = defaultdict(int)
        ca = defaultdict(int)

        m1 = defaultdict(int)
        m2 = defaultdict(int)
        m3 = defaultdict(int)

        re = 0

        for i in range(n - 2):
            a, b, c = arr[i], arr[i + 1], arr[i + 2]
            ab[(a, b)] += 1
            bc[(b, c)] += 1
            ca[(c, a)] += 1

            triple = (a, b, c)
            m1[triple] += 1
            m2[triple] += 1
            m3[triple] += 1

            re += ab[(a, b)] - m1[triple]
            re += bc[(b, c)] - m2[triple]
            re += ca[(c, a)] - m3[triple]

        print(re)
