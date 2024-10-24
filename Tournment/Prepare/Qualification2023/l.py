#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, b = input().split()
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        print(cnt)
