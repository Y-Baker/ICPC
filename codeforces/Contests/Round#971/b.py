#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict, deque
from math import ceil


if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        cnt = 0
        xTops = set()
        xBottoms = set()
        for _ in range(n):
            x, y = map(int, input().split())
            if y == 0:
                xBottoms.add(x)
            else:
                xTops.add(x)
        cnt = 0
        for one in xTops:
            if one in xBottoms:
                cnt += n - 2

        # الخارج من القايمة نص طول الوتر
        for one in xTops:
            if (one - 1) in xBottoms and (one + 1) in xBottoms:
                cnt += 1

        for one in xBottoms:
            if (one - 1) in xTops and (one + 1) in xTops:
                cnt += 1
        print(cnt)
