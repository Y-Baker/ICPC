#!/usr/bin/python3

from collections import defaultdict
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(input())
        mapp = defaultdict(int)
        for one in arr:
            mapp[one] += 1
        cnt = 0
        problems = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        while m > 0:
            for problem in problems:
                if mapp[problem] > 0:
                    mapp[problem] -= 1
                else:
                    cnt += 1
            m -= 1
        print(cnt)
