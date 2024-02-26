#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        ss = ''
        for i, c in enumerate(s):
            if i == 0 or i == len(s) - 1:
                ss += c
            else:
                if i % 2 == 1:
                    ss += c
        print(ss)
