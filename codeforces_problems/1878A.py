#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        if k in arr:
            print("YES")
        else:
            print("NO")
