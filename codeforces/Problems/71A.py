#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        if len(s) > 10:
            print(s[0] + str(len(s) - 2) + s[-1])
        else:
            print(s)

