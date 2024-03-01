#!/usr/bin/python3

if __name__ == '__main__':
    t = 1

    for _ in range(t):
        s = input()
        count = 0
        ptr = 'a'
        for c in s:
            count += min(abs(ord(c) - ord(ptr)), 26 - abs(ord(c) - ord(ptr)))
            ptr = c
        print(count)
