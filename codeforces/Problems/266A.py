#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        cnt = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cnt += 1
        print(cnt)

