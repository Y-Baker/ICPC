#!/usr/bin/python3

from collections import defaultdict
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        curr = 1
        start = 0
        max_start = 0
        maxx = 1
        for idx in range(1, len(s)):
            if s[idx] == s[start]:
                curr += 1
            else:
                if curr > maxx:
                    maxx = curr
                    max_start = start
                start = idx
                curr = 1
        if curr > maxx:
            maxx = curr
            max_start = start
        

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in letters:
            if i not in s:
                distinct = i
                break
        if maxx == 1:
            print(distinct + s)
        else:
            idx = max_start + 1
            print(s[:idx] + distinct + s[idx:])
