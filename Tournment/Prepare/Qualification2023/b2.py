#!/usr/bin/python3

from collections import deque
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = input().strip()
        ans = deque()
        curr = ''
        flag = True
        s += '>'
        for c in s:
            if c == '<':
                if flag:
                    ans.append(curr)
                else:
                    ans.appendleft(curr)
                curr = ''
                flag = False
            elif c == '>':
                if flag:
                    ans.append(curr)
                else:
                    ans.appendleft(curr)
                curr = ''
                flag = True
            else:
                curr += c
        
        print(''.join(ans))

