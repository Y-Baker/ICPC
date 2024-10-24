#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        cnt = 0
        i = 0
        while i < n:
            if s[i] == 'B':
                i += k
                cnt += 1
            else:
                i += 1

        print(cnt)
