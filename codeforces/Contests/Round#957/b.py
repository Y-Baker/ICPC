#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        maxx = 0
        for i in range(k):
            if arr[i] > arr[maxx]:
                maxx = i
        cnt = 0
        for i in range(k):
            if i != maxx:
                cnt += (arr[i] - 1) + arr[i]
        print(cnt)


