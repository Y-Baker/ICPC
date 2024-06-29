#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s1 = input()
        s2 = input()
        s1 = s1.lower()
        s2 = s2.lower()
        if s1 < s2:
            print(-1)
        elif s1 > s2:
            print(1)
        else:
            print(0)

