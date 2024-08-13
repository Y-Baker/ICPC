#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        t = input()
        res = ''
        flag = False
        p1 = 0
        p2 = 0
        while p1 < len(s):
            if p2 == len(t):
                flag = True
                for i in range(p1, len(s)):
                    if s[i] == '?':
                        res += 'a'
                    else:
                        res += s[i]
                break
            if s[p1] == t[p2]:
                p2 += 1
            else:
                if s[p1] == '?':
                    res += t[p2]
                    p2 += 1
                    p1 += 1
                    continue
            res += s[p1]
            p1 += 1
        if p2 >= len(t) and not flag:
            flag = True
            for i in range(p1, len(s)):
                if s[i] == '?':
                    res += 'a'
                else:
                    res += s[i]
        if not flag:
            print('NO')
        else:
            print('YES')
            print(res)
