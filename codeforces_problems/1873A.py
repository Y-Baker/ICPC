#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        should = 'abc'
        cnt = 0
        for i in range(3):
            if s[i] == should[i]:
                cnt += 1
        if cnt >= 1:
            print('YES')
        else:
            print('NO')
