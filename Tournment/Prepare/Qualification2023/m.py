#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        l, n, one = map(int, input().split())
        q = int(input())
        arr = list(map(int, input().split()))

        sections = [(0, l)]
        for i in arr:
            

