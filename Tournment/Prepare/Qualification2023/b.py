#!/usr/bin/python3

from collections import deque
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = input().strip()
        arr1 = []
        arr2 = deque()

        curr = ''
        s+='<'
        for c in s:
            if c != '<' and c != '>':
                curr += c
            if c == '<':
                arr1.append(curr)
                curr = ''
            elif c == '>':
                arr2.appendleft(curr)
                curr = ''
        print(''.join(arr2) + ''.join(arr1))            

