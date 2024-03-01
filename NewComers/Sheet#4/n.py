#!/usr/bin/python3
from collections import deque

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, m = list(map(int, input().split()))
        s = input()
        def getsub(s):
            ss = ''
            l = 0
            r = len(s) - 1
            q1 = deque()
            q2 = deque()
            while l < r:
                q1.append(s[l])
                q2.appendleft(s[r])
                if q1 == q2:
                    ss = ''.join(q1)
                l += 1
                r -= 1

            return s[len(ss):]

        ss = getsub(s)

        re = s + ss * (m - 1)

        print(re)

