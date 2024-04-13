#!/usr/bin/python3
from collections import deque
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        mapp = {}
        for i in range(n):
            s = input()

            mapp[s] = mapp.get(s, 0) + 1

        x1 = deque()
        x2 = ''
        x3 = ''
        for k, v in mapp.items():
            if k[::-1] in mapp and mapp[k[::-1]] > 0 and k != k[::-1]:
                x1.appendleft(k)
                x2 += k[::-1]
                mapp[k[::-1]] -= 1
            elif k == k[::-1] and mapp[k] > 0:
                x3 = k
            mapp[k] -= 1

        x1 = ''.join(x1)
        print(len(x1 + x3 + x2))
        print(x1 + x3 + x2)

